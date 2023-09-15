import React from "react";
import { RiMapPin2Line } from "react-icons/ri";
import { useRouter } from "next/navigation";

import Image from "next/image";

interface CardProps {
    data: {
        id: number;
        publication_date: string;
        city: string;
        pet_publication: {
            name: string;
        }
        image_publication: {
            url: string;
        }
    }; 
    lblname: boolean;
    lbllocation: boolean;
    lbltime: boolean;
    lbldesc: boolean;
    link: string;
}

const Card: React.FC<CardProps> = ({ data, lblname, lbllocation, lbltime, lbldesc, link }) => {

    console.log(data);

    const router = useRouter();

    const handleClick = () => {
        router.push(`${link}/${data.id}`);
    };

    return (
        <div 
            className="cursor-pointer border-[1px] border-gray-200 bg-white p-4 rounded-lg shadow-md my-4 mx-2 hover:border-[1px] hover:border-color3-500 transition-all duration-300 hover:scale-105 hover:bg-color3-50/10"
            onClick={handleClick}
        >
            <Image 
                src={data.image_publication.url} 
                alt={data.pet_publication.name} 
                className="w-[250px] h-[200px] object-cover rounded-lg" 
                priority={false} 
                width={200}
                height={200}
            /> 
            <div className="mt-2 text-gray-500 text-left">
                { lblname && <p className="font-semibold">{data.pet_publication.name}</p> }
                { lbldesc && <p className="font-semibold text-gray-400">{data.pet_publication.name}</p> }
                { lbllocation && <p className="text-xs flex flex-row items-center gap-1 text-gray-400 mb-2"><RiMapPin2Line className="text-color3-500" />{data.address}</p> }
                { lbltime && <p className="text-xs flex flex-row items-center gap-1 font-semibold">{data.publication_date}</p> }
            </div>
        </div>
    );
};

export default Card;
