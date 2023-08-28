import React from "react";
import { IoMdPin } from "react-icons/io";
import { BsCalendar3 } from "react-icons/bs";
import { RiMapPin2Line } from "react-icons/ri";

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
        <div className="cursor-pointer border-[1px] border-gray-300 bg-white p-4 rounded-lg shadow-md my-4 mx-2 ">
            <Image 
                src={data.image} 
                alt={data.name} 
                className="w-[250px] h-[200px] object-cover rounded-lg" 
                priority={false} 
                width={200}
                height={200}
            /> 
            <div className="mt-2 text-gray-500 text-left">
                { lblname && <p className="font-semibold">{data.name}</p> }
                { lbldesc && <p className="font-semibold text-gray-400">{data.desc}</p> }
                { lbllocation && <p className="text-xs flex flex-row items-center gap-1 text-gray-400 mb-2"><RiMapPin2Line className="text-color3-500" />{data.location}</p> }
                { lbltime && <p className="text-xs flex flex-row items-center gap-1 font-semibold">{data.time}</p> }
            </div>
        </div>
    );
};

export default Card;
