'use client'
import Carrusel from './carrusel';
import React, { useState, useEffect } from "react";

export default function Perdidos() {

    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async() => {
            setIsLoading(true);
            setError(null);

            try {
                const response = await fetch(process.env.ENDPOINT_API+'carouselAdopciones/?page=1&size=9');
                if (!response.ok) {
                    throw new Error('Unable to fetch data');
                }
                const data = await response.json();
                console.log('Data from API:', data); // Log the data
                setData(data);
            } catch (err) {
                console.error('Error:', err); // Log the error
                setError(err.message);
            }

            setIsLoading(false);
        };
        
        fetchData();        
    }, []);
    
    console.log(data);

    return <Carrusel 
                title="Perdidos" 
                data={data} 
                lblname={true}
                lbllocation={true}
                lbltime={true}
                lbldesc={false}
                link="/perdidos"
            /> 

}
