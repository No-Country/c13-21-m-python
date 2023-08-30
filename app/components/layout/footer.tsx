import { logo } from '@public/assets';
import { BsFacebook, BsInstagram} from 'react-icons/bs';

import Image from 'next/image';

export default function Footer() {
    return <footer className="w-full bg-[#FED615] py-8">
        <div className="flex flex-row items-center justify-between px-32">
            <div className='text-white gap-y-2'>
                <Image src={logo.src} alt="PetFinder" className="w-[25px] mb-2" width={100} height={100} />
                <p> ✉️  <span className='font-bold text-color2-700'>staff@petfinder.com</span></p>
                <p> 📞 <span>(+52) 777 266 95 45</span></p>
                <p> 🇲🇽 <span>Cuernavaca, Morelos, México</span></p>
            </div>
            <div className='flex flex-col'>
                <div className='flex flex-row items-end justify-end gap-2 text-xl text-white pb-2'>
                   <BsFacebook />
                   <BsInstagram />
                </div>
                <div className='text-white'>
                    <a href='#'>
                        Aviso de privacidad
                    </a>
                </div>
            </div>
        </div>
    </footer>
}