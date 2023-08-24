import React from "react";
import { IoMdPin } from "react-icons/io";
import { BsCalendar3 } from "react-icons/bs";

import Image, { StaticImageData } from "next/image";

interface CardProps {
    image: StaticImageData;
    petName: string;
}

const Card: React.FC<CardProps> = ({ image, petName }) => {
    return (
        <div className="cursor-pointer border-[1px] border-gray-300 bg-white p-4 rounded-lg shadow-md my-4 mx-2 ">
            <Image src={image} alt={petName} className="w-[250px] h-[200px] object-cover rounded-lg" /> 
            <div className="mt-2 text-gray-500 text-left">
                <p className="font-bold mb-1">{petName}</p>
                <p className="text-sm flex flex-row items-center gap-1 text-gray-400 mb-1"><IoMdPin className="text-mainyellow-500" />Castelar, Bs. A.s.</p>
                <p className="text-sm flex flex-row items-center gap-1 text-gray-400 text-mainpurple-500 font-semibold"> Hace 5 días</p>
            </div>
        </div>
    );
};

export default Card;