'use client'
import Carrusel from './carrusel';
import React, { useState, useEffect } from "react";
import useSWR from "swr";

async function fetcherFunction(url: RequestInfo | URL) {
    try {
      const response = await fetch(url);
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
}

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
