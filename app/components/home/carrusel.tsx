'use client'
import { Swiper, SwiperSlide } from "swiper/react"
import { Navigation, Mousewheel, Keyboard } from 'swiper/modules';
import 'swiper/css'
import 'swiper/css/navigation';
import 'swiper/css/pagination';

import  { BsChevronCompactRight } from 'react-icons/bs';
import Card from './card';

import Link from "next/link";

interface CardProps {
    title: string;
    data: Array<{
        id: number;
        name: string;
        desc: string;
        img: string;
        time: string;
        location: string;
    }>;
    link: string;
    lblname: boolean;
    lbllocation: boolean;
    lbltime: boolean;
    lbldesc: boolean;
}

const Carrusel: React.FC<CardProps> = ({ title, data, link, lblname, lbllocation, lbltime, lbldesc }) => {

    return <div className="mx-32 text-center pb-8">

        <div className='flex flex-row items-center justify-between px-2'>
            <div className="carrousel-title">{title}</div>
            <Link href={link} className='btn flex items-center gap-1'> Ver todos <BsChevronCompactRight className='text-gray-300' /> </Link>
        </div>

        <div className="w-[1240px] flex flex-row justify-center items-center gap-[3rem] mb-6">
            <Swiper
                slidesPerView={5}
                spaceBetween={1}
                pagination={{
                    clickable: true,
                }}
                navigation={true}
                mousewheel={true}
                keyboard={true}
                modules={[Navigation, Mousewheel, Keyboard]}
                className="carruselSwiper"
            >
            {
                data.map((d, index) => (
                    <SwiperSlide key={index}>
                        <Card
                            data={d}
                            lblname={lblname}
                            lbllocation={lbllocation}
                            lbltime={lbltime}
                            lbldesc={lbldesc}
                            link={link}
                        />

                    </SwiperSlide>
                ))
            }
            </Swiper>
        </div>

      </div>

}

export default Carrusel;
