'use client'
import Carrusel from './carrusel';
import React, { useState, useEffect } from "react";
import useSWR from "swr";

export default function Encontrados() {

    const fetcher = (url: RequestInfo | URL) => fetch(url).then((res) => res.json());
    const { data, error, isLoading } = useSWR('http://50.18.105.237:5000/api/carouselEncontrados/?page=1&size=9', fetcher);
 
    if (error) return <div>Failed to load</div>
    if (isLoading) return <div>Loading...</div>
    console.log(data);

    return <Carrusel 
                title="Encontrados" 
                data={data} 
                lblname={false}
                lbllocation={true}
                lbltime={true}
                lbldesc={false}
                link='/encontrados'
            /> 

}