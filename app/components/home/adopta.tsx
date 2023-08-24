'use client'
import React, { useRef, useState } from 'react'
import { adopta1, adopta2, adopta3 } from "@public/assets"
import { Swiper, SwiperSlide } from "swiper/react"
import { Navigation, Pagination, Mousewheel, Keyboard } from 'swiper/modules';
import 'swiper/css'
import 'swiper/css/navigation';
import 'swiper/css/pagination';

import Card from './card';

export default function Adopta() {

    const data = [
        {
            id: 1,
            name: 'Rosenda',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta1
        },
        {
            id: 2,
            name: 'Wasabi',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta2
        },
        {
            id: 3,
            name: 'Tampico',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta3
        },
        {
            id: 4,
            name: 'Rosenda',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta1
        },
        {
            id: 5,
            name: 'Wasabi',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta2
        },
        {
            id: 6,
            name: 'Tampico',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta3
        },
        {
            id: 7,
            name: 'Rosenda',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta1 
        },
        {
            id: 8,
            name: 'Wasabi',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta2
        },
        {
            id: 9,
            name: 'Tampico',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: adopta3
        },
    ]


    return <div className="mx-32 text-center py-32">
        <h1 className="text-3xl font-bold text-cyan-500">ADOPTA HOY, CAMBIA UNA VIDA</h1>
        <h2 className="text-2xl text-gray-500">CONOCE A LAS MASCOTAS EN ADOPCIÓN</h2>

        <div className="w-[1240px] flex flex-row justify-center items-center py-8 gap-[3rem] m-6">
                        
            <Swiper
            cssMode={true}
                slidesPerView={5}
                spaceBetween={30}
                pagination={{
                    clickable: true,
                }}
                navigation={true}
                mousewheel={true}
                keyboard={true}
                modules={[Navigation, Mousewheel, Keyboard]}
                className="adoptaSwiper"
            >
            {
                data.map((d, index) => (
                    <SwiperSlide>
                        <Card image={d.image} petName={d.name} />
                    </SwiperSlide>
                ))
            }

        
      </Swiper>
        </div>

        <div className="flex flex-row gap-[3rem] mt-6">
            { /* data.map((d, index) => (
                    <div className=" hover:scale-110 hover:drop-shadow-lg transition-all cursor-pointer">
                        <img src={d.image} alt={d.name} className="w-[250px] h-[250px] object-cover rounded-md" /> 
                        <div className="mt-2 text-gray-500">{d.name}</div>
                    </div>
                ))
            */ }
        </div>

        <div>
            <button className=" bg-yellow-600 text-white px-4 py-2 rounded-md mt-6">VER TODOS</button>
        </div>

        <div>
          Hola mundo!
        </div>

      </div>

}
