import React from "react"
import { Map, Marker } from "pigeon-maps"

export default function MyMap() {

    const handleClick = (e: any) =>{
        console.log(e.latLng);
    } 

  return (
    <Map height={400} defaultCenter={[18.8629,-99.2152]} defaultZoom={17} onClick={handleClick}>
      <Marker width={50} anchor={[18.862920609479993,-99.21523396473492]} color='red' />
    </Map>
  )
}