'use client'

import Carrusel from './carrusel';
import { data } from '@utils/data.js';

export default function Perdidos() {

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
