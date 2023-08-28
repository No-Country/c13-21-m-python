'use client'

import Carrusel from './carrusel';
import { data } from '@utils/data.js';

export default function Encontrados() {

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