import React from "react";
import { RiMapPin2Line } from "react-icons/ri";

import Image from "next/image";

interface CardProps {
    data: any; 
    lblname: boolean;
    lbllocation: boolean;
    lbltime: boolean;
    lbldesc: boolean;
}

const Card: React.FC<CardProps> = ({ data, lblname, lbllocation, lbltime, lbldesc }) => {

    console.log(data);

    return (
        <div className="cursor-pointer border-[1px] border-gray-300 bg-white p-4 rounded-lg shadow-md my-4 mx-2 ">
            <Image 
                src={data.img} 
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
