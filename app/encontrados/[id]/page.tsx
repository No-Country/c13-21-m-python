'use client'
import { useEffect, useState } from "react";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import { RiMapPin2Line } from "react-icons/ri";
import { BsGenderFemale, BsGenderMale } from "react-icons/bs";

import { icon_cat, icon_dog } from "@/public/assets";

import MyMap from "@components/page/map";

import useSWR from 'swr';
import fetcherFunction from "@/app/fetcherFunction"

export default function Page({ params }: { params: any }) {

    const router = useRouter();
    const id = params.id;

    const { data, error } = useSWR('http://50.18.105.237:5000/api/publications/'+id, fetcherFunction);

    console.log('URL being fetched:', 'http://50.18.105.237:5000/api/publications/'+id);
 
    if (error) {
        return <div>Error fetching data</div>;
    }
    
    if (!data) {
        return <div>Loading...</div>;
    }

    console.log(data);

    const publication = data.publication
    console.log(publication)

    return (
        <div className="pageContainer">

            <div className="container">

                <h1
                    className="text-3xl font-semibold text-gray-700 text-center py-6"
                >
                    Encontrados
                </h1>

                { !publication.id ? <div className="w-full h-[100vh]">Loading...</div> : <> 

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
                        { publication.publication_date }
                    </div>
                </div>

                <div className="flex my-16">
                    <div className="w-[40%] pr-[5%]">
                        <div className="py-4 flex flex-col justify-between items-start border-b-[1px] border-gray-200">

                            <h1 className="text-4xl font-semibold text-gray-700 pb-4">{ publication.pet_publication.name }</h1>
                            <div className="wrap-atributes pb-4">
                                <div className="atribute-lg">
                                    { publication.pet_publication.type === 'Perro' && <><Image className="w-[14px]" src={icon_dog} alt="dog" width={100} height={100} /> Perro</> }
                                    { publication.pet_publication.type === 'Gato' && <><Image className="w-[14px]" src={icon_cat} alt="cat" width={100} height={100} /> Gato</> }
                                </div>
                                <div className="atribute-lg">
                                    { publication.pet_publication.genre === 'macho' && <><BsGenderMale className="text-color3-500 text-sm" /> Macho</> }
                                    { publication.pet_publication.genre === 'hembra' && <><BsGenderFemale className="text-color3-500 text-sm" /> Hembra</> }
                                </div>
                            </div>
                            <div className="flex items-center justify-center gap-1 py-2">
                                <RiMapPin2Line className="text-color3-500 text-[16px]" />
                                <span className="text-sm">{publication.address}</span>
                            </div>

                        </div>
                        <div className="mt-4 mb-8 pt-4 pb-16 border-b-[1px] border-gray-200">
                            { publication.pet_publication.description }
                        </div>

                        <div>
                            <h2 className="text-md font-semibold text-gray-700 mb-4">
                                Datos de contacto
                            </h2>
                            <p>{publication.name}</p>
                            <p>{publication.phone}</p>
                        </div>

                    </div>
                    <div className="w-[60%]">
                        <div
                            className="bg-gray-100 h-[60vh] overflow-hidden flex justify-center items-center rounded-2xl bg-[${state.img}] bg-cover bg-center"
                            style={{backgroundImage: `url(${publication.image_publication[0].url})`}}
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