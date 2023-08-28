'use client'

import React, { useRef, useState } from 'react';
// Import Swiper React components
import { Swiper, SwiperSlide } from 'swiper/react';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

// import required modules
import { Autoplay, Pagination, Navigation } from 'swiper/modules';

import { header1, header2 } from "@public/assets";


export default function HomeSlider() {

    const slides = [
        {
            id: 1,
            src: header1,
            alt: "foto1",
            content: '<div class="absolute left-[35rem] bottom-[10rem] flex items-center gap-5"><a href="#" class="bg-white text-sm text-color3-500 rounded-full px-4 py-2">Ver perdidos</a><a href="#" class="bg-white text-sm text-color3-500 rounded-full px-4 py-2">Ver encontrados</a><div>'
        },
        {
            id: 2,
            src: header2,
            alt: "foto2",
            content: '<div class="absolute left-[35rem] bottom-[10rem] flex items-center gap-5"><a href="#" class="bg-white text-sm text-color3-500 rounded-full px-4 py-2">Ver publicaciones</a><div>'
        },
      ]


    

    return <div className="w-[1280px] h-[540px] relative group mb-8">

         <Swiper
        spaceBetween={1}
        centeredSlides={true}
        autoplay={{
          delay: 4500,
          disableOnInteraction: false,
        }}
        pagination={{
          clickable: true,
        }}
        modules={[Autoplay, Pagination, Navigation]}
        className="homeSwiper"
      >
        <SwiperSlide>
            <div className='w-[1280px] h-[520px]' style={{backgroundImage: `url(${header1.src})`}}>
            </div>
        </SwiperSlide>
        <SwiperSlide>
            <div className='w-[1280px] h-[520px]' style={{backgroundImage: `url(${header2.src})`}}>
            </div>
        </SwiperSlide>
      </Swiper> 

    </div>
}
