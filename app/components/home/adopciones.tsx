'use client'
import Carrusel from './carrusel';
import React, { useState, useEffect } from "react";
import useSWR from "swr";
import fetcherFunction from "@/app/fetcherFunction"

export default function Adopciones(){

    const { data, error } = useSWR('http://50.18.105.237:5000/api/carouselAdopciones/?page=1&size=9', fetcherFunction);
 
    if (error) {
        return <div>Error fetching data</div>;
    }
    
    if (!data) {
        return <div>Loading...</div>;
    }

    console.log(data);

    return <Carrusel 
                title="Adopciones" 
                data={data} 
                lblname={false}
                lbllocation={true}
                lbltime={true}
                lbldesc={true}
                link='/adopciones'
            /> 

}
