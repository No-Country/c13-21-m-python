'use client'

import Carrusel from './carrusel';
import { data } from '@utils/data.js';


export default function Adopciones(){

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
