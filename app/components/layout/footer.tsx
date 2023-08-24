import { logo } from '@public/assets'
import { BsFacebook, BsInstagram} from 'react-icons/bs'

export default function Footer() {
    return <footer className="w-full bg-[#FED615] py-8">
        <div className="flex flex-row items-center justify-between px-32">
            <div className='text-white gap-y-2'>
                <img src={logo.src} alt="PetFinder" className="w-[90px] mb-2" />
                <p> ✉️  <span className='font-bold text-mainyellow-700'>staff@petfinder.com</span></p>
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