'use client';

import { log } from "console";
// import Image from "next/image";
import Link from "next/link";
import { usePathname } from 'next/navigation'
// import { useEffect } from "react";
// import { logo } from "@public/assets"
import { AiOutlineUser } from 'react-icons/ai';
import { CiSearch } from 'react-icons/ci';
import { BsDot } from 'react-icons/bs';

export default function Navbar() {

  const pathname = usePathname();
  console.log(pathname);

  return (
    
    <div className="navbar">
      <div className="w-[1240px] h-full mx-auto py-1 font-titleFont flex items-center justify-between">
        <div className="flex flex-row items-center">
          {/* <Image src={logo} className="w-[4rem] mr-3" alt="logo_app" /> */}
          <Link href="/" className="text-xl font-bold text-maingreen-500">
            PetFinder
          </Link>
        </div>

        <ul className="menu">
            <li>
              <Link href="perdidos" className={ ( pathname === '/perdidos' ? 'active' : '' ) }>
                <span className="text">Perdidos</span>
                <span className="dot"><BsDot /></span>
              </Link>
            </li>
            <li>
              <Link href="encontrados" className={ ( pathname === '/encontrados' ? 'active' : '' ) }>
                <span className="text">Encontrados</span>
                <span className="dot"><BsDot /></span>
              </Link>
            </li>
            <li>
              <Link href="adopciones" className={ ( pathname === '/adopciones' ? 'active' : '' ) }>
                <span className="text">Adopciones</span>
                <span className="dot"><BsDot /></span>
              </Link>
            </li>
        </ul>

        <div className="flex items-center gap-2">
        <div className="group-search">
          <input className="inp-search" type="text" />
          <CiSearch className="search-icon" />
        </div>
              <button className="btn-login flex items-center gap-1">
                <AiOutlineUser className="text-maingreen-500" />
              </button>
        </div>
      </div>
    </div>);
}