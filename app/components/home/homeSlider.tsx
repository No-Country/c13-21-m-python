'use client'

import { useState, useEffect } from "react";
import { header1, header2 } from "@public/assets";

import  { BsChevronCompactLeft, BsChevronCompactRight } from 'react-icons/bs';
import { RxDotFilled } from 'react-icons/rx';

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

    const [current, setCurrent] = useState(0)

    const handleNextSlide = () => {
        setCurrent(current === slides.length - 1 ? 0 : current + 1)
    }

    const handlePrevSlide = () => {
        setCurrent(current === 0 ? slides.length - 1 : current - 1)
    }

    /*
    useEffect(() => {
        const interval = setInterval(() => handleNextSlide(), 3500);
        return () => clearInterval(interval);
        // eslint-disable-next-line no-use-before-define
    }, [current])
*/

    return <div className="w-[1360px] h-[600px] relative group pb-20">
        <div 
            style={{backgroundImage: `url(${slides[current].src.src})`}}
            className="w-full h-full bg-center bg-cover duration-1000 mt-4" 
        >
        
            <div className="flex flex-col justify-center h-full w-ful text-white text-[2rem] font-semibold" dangerouslySetInnerHTML={{__html:slides[current].content}} />

            <div className="flex bottom-4 items-center justify-center py-[.2rem] px-4 rounded-md bg-white/30">
                {slides.map((slide, index) => (
                    <div key={index}>
                        <RxDotFilled 
                            key={index}
                            className={`text-2xl cursor-pointer ${index === current ? "text-maingreen-500" : "text-black"}`}
                            onClick={() => setCurrent(index)}
                        />
                    </div>
                ))}
            </div>

        </div>

        <div 
            className="hidden group-hover:block absolute top-[50%] -translate-x-0 translate-y-[-50%] left-5 text-2xl rounded-full p-2 bg-black/20 text-white cursor-pointer"
            onClick={handlePrevSlide} 
        >
            <BsChevronCompactLeft />
        </div>

        <div 
            className="hidden group-hover:block absolute top-[50%] -translate-x-0 translate-y-[-50%] right-5 text-2xl rounded-full p-2 bg-black/20 text-white cursor-pointer"
            onClick={handleNextSlide}
        >
            <BsChevronCompactRight />
        </div>

        

    </div>
}
