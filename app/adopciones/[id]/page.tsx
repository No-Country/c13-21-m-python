'use client';
import { useEffect, useState } from "react";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import { RiMapPin2Line } from "react-icons/ri";
import { BsGenderFemale, BsGenderMale } from "react-icons/bs";

import { icon_cat, icon_dog } from "@/public/assets";

import { data}  from '@utils/data';
import MyMap from "@components/page/map";

export default function Page({ params }: { params: any }) {

    const router = useRouter();
    const [state, setState] = useState<any>({});

    useEffect(() => {
        
        const id = params.id;
        const filtered = data.filter((item) => item.id == +id);

        setState(filtered[0]);

        // eslint-disable-next-line no-use-before-define
    }, [params.id]);

    return (
        <div className="pageContainer">

            <div className="container">

                <h1
                    className="text-3xl font-semibold text-gray-700 text-center py-6"
                >
                    Adopciones
                </h1>

                { !state.id ? <div className="w-full h-[100vh]">loading...</div> : <> 

                <div className="page-topbar duration-1000 ">
                    <div className='flex items-center gap-1'>
                        <button 
                            className="btn text-xl font-semibold"
                            onClick={() => router.back()}     
                        >
                            <FaChevronLeft /> Volver
                        </button>
                    </div>
                    <div>
                        { state.date }
                    </div>
                </div>

                <div className="flex my-16">
                    <div className="w-[40%] pr-[5%]">
                        <div className="py-4 flex flex-col justify-between items-start border-b-[1px] border-gray-200">

                            <h1 className="text-4xl font-semibold text-gray-700 pb-4">{ state.name }</h1>
                            <div className="wrap-atributes pb-4">
                                <div className="atribute-lg">
                                    { state.type === 'dog' && <><Image className="w-[14px]" src={icon_dog} alt="dog" width={100} height={100} /> Perro</> }
                                    { state.type === 'cat' && <><Image className="w-[14px]" src={icon_cat} alt="cat" width={100} height={100} /> Gato</> }
                                </div>
                                <div className="atribute-lg">
                                    { state.sex === 'male' && <><BsGenderMale className="text-color3-500 text-sm" /> Macho</> }
                                    { state.sex === 'female' && <><BsGenderFemale className="text-color3-500 text-sm" /> Hembra</> }
                                </div>
                            </div>
                            <div className="flex items-center justify-center gap-1 py-2">
                                <RiMapPin2Line className="text-color3-500 text-[16px]" />
                                <span className="text-sm">{state.location}</span>
                            </div>

                        </div>
                        <div className="mt-4 mb-8 pt-4 pb-16 border-b-[1px] border-gray-200">
                            { state.fullDescription }
                        </div>

                        <div>
                            <h2 className="text-md font-semibold text-gray-700 mb-4">
                                Datos de contacto
                            </h2>
                            <p>{state.contact_name}</p>
                            <p>{state.contact_phone}</p>
                        </div>

                    </div>
                    <div className="w-[60%]">
                        <div
                            className="bg-gray-100 h-[60vh] overflow-hidden flex justify-center items-center rounded-2xl bg-[${state.img}] bg-cover bg-center"
                            style={{backgroundImage: `url(${state.img})`}} 
                        >
                            {/* 
                            <Image src={state.img} alt={state.name} width={500} height={500} className="h-full w-[150%]" />
                            */}
                        </div>
                    </div>

                    
                </div> 

                <div>
                    
                    <h2 className="text-4xl font-semibold text-gray-700 mb-4">
                        Visto por última vez
                    </h2>

                    <div className="map-container w-full h-[400px] bg-gray-100 rounded-2xl mb-16 overflow-hidden">
                        <MyMap />
                    </div>    
                        
                </div>

                </>}
            </div>
        </div>
    )
}