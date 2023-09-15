'use client';
import React from "react";
import { useRouter } from "next/navigation";

import { RiMapPin2Line } from "react-icons/ri";
import { BsGenderFemale, BsGenderMale } from "react-icons/bs";

import { icon_cat, icon_dog } from "@/public/assets";

import Image from "next/image";

interface CardProps {
    data: { 
        id: number,
        publication_date: string,
        address: string,
        pet_publication: {
            type: string,
            name: string,
            genre: string,
            description: string
        },
        image_publication: [
            {
                url: string
            }
        ]
        };
        key: number;
        link: string;
   
}

const Card: React.FC<CardProps> = ({ data, link }) => {

    const router = useRouter();

    const handleClick = () => {
        router.push(`${link}/${data.id}`);
    }

    return (
        <div
            onClick={handleClick} 
            className="w-[32%] cursor-pointer border-[1px] border-gray-300 bg-white rounded-lg shadow-md my-4 flex flex-col hover:border-color3-500 transition duration-300 ease-in-out hover:scale-105 hover:shadow-2xl"
        >
            <div className="p-4 overflow-hidden flex w-[410px] h-[410px]">
                <Image 
                    src={data.image_publication[0].url} 
                    alt={data.pet_publication.name} 
                    className="w-full object-cover rounded-lg overflow-hidden" 
                    priority={false} 
                    width={500}
                    height={500}
                /> 
            </div>

            <div className="flex justify-between mt-2 border-gray-100 border-b-2 px-4 pb-4">
                <h3 className="text-lg font-semibold text-gray-500">{data.pet_publication.name}</h3>
                <div className="wrap-atributes">
                    <div className="atribute">
                        { data.pet_publication.type === 'Perro' && <><Image className="w-[14px]" src={icon_dog} alt="dog" width={100} height={100} /> Perro</> }
                        { data.pet_publication.type === 'Gato' && <><Image className="w-[14px]" src={icon_cat} alt="cat" width={100} height={100} /> Gato</> }
                    </div>
                    <div className="atribute">
                        { data.pet_publication.genre === 'macho' && <><BsGenderMale className="text-color3-500 text-sm" /> Macho</> }
                        { data.pet_publication.genre === 'hembra' && <><BsGenderFemale className="text-color3-500 text-sm" /> Hembra</> }
                    </div>
                </div>
            </div>

            <div className="flex justify-between text-sm text-gray-400 font-semibold">
                <div className="flex items-center justify-center gap-1 px-4 py-2">
                    <RiMapPin2Line className="text-color3-500 text-[16px]" />
                    <span className="text-sm">{data.address}</span>
                </div>
                <div className="flex items-center gap-2 px-4 py-2">
                    <span className="text-sm">{data.publication_date}</span>
                </div>
            </div>

            <div className="p-4 text-xs text-gray-500">
                <p className="line-clamp-2">
                    {data.pet_publication.description}
                </p>
            </div>
            
        </div>
    );
};

export default Card;