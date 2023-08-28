import React from "react";
import { RiMapPin2Line } from "react-icons/ri";
import { BsGenderFemale, BsGenderMale } from "react-icons/bs";

import { icon_cat, icon_dog } from "@/public/assets";

import Image, { StaticImageData } from "next/image";

interface CardProps {
    data: Array<{
        id: number;
        name: string;
        desc: string;
        image: string;
        time: string;
    }>;
    lblname: boolean;
    lbllocation: boolean;
    lbltime: boolean;
    lbldesc: boolean;
}

const Card: React.FC<CardProps> = ({ data, lblname, lbllocation, lbltime, lbldesc }) => {

    return (
        <div className="w-[32%] cursor-pointer border-[1px] border-gray-300 bg-white rounded-lg shadow-md my-4 flex flex-col">
            <div className="p-4 overflow-hidden flex w-[410px] h-[410px]">
                <Image 
                    src={data.image} 
                    alt={data.name} 
                    className="w-full object-cover rounded-lg overflow-hidden" 
                    priority={false} 
                    width={500}
                    height={500}
                /> 
            </div>

            <div className="flex justify-between mt-2 border-gray-100 border-b-2 px-4 pb-4">
                <h3 className="text-lg font-semibold text-gray-500">{data.name}</h3>
                <div className="wrap-atributes">
                    <div className="atribute">
                        { data.type === 'dog' && <><Image className="w-[14px]" src={icon_dog} alt="dog" width={100} height={100} /> Perro</> }
                        { data.type === 'cat' && <><Image className="w-[14px]" src={icon_cat} alt="cat" width={100} height={100} /> Gato</> }
                    </div>
                    <div className="atribute">
                        { data.sex === 'male' && <><BsGenderMale className="text-color3-500 text-sm" /> Macho</> }
                        { data.sex === 'female' && <><BsGenderFemale className="text-color3-500 text-sm" /> Hembra</> }
                    </div>
                </div>
            </div>

            <div className="flex justify-between text-sm text-gray-400 font-semibold">
                <div className="flex items-center justify-center gap-1 px-4 py-2">
                    <RiMapPin2Line className="text-color3-500 text-[16px]" />
                    <span className="text-sm">{data.location}</span>
                </div>
                <div className="flex items-center gap-2 px-4 py-2">
                    <span className="text-sm">{data.date}</span>
                </div>
            </div>

            <div className="p-4 text-xs text-gray-500">
                <p className="line-clamp-2">
                    {data.fullDescription}
                </p>
            </div>
            
        </div>
    );
};

export default Card;