import { info1,info2, info3, info4 } from "@public/assets"

export default function Info() {
    return <div className="w-full py-32">
        <div className="px-32 flex flex-row justify-center gap-6">
            <div className="w-[250px] h-[250px] rounded-[50%] bg-slate-200 bg-cover bg-bottom overflow-hidden flex flex-col items-center justify-start pt-[2rem]" style={{backgroundImage: `url(${info1.src})`}}>
                <p className="max-w-[20ch] text-center text-sm text-gray-700">Mira los perros y gatos que tenemos en adopción</p>
                <button className="mt-2 bg-white/50 rounded-md px-4 text-gray-500 hover:text-cyan-500 transition-all hover:bg-white">ADOPTA AQUÍ</button>
            </div>

            <div className="w-[250px] h-[250px] rounded-[50%] bg-slate-200 bg-cover bg-right overflow-hidden flex flex-col items-center justify-start pt-[2rem]" style={{backgroundImage: `url(${info4.src})`}}>
                <p className="max-w-[20ch] text-center text-sm text-gray-700">¿Te gustaría adoptar? conoce nuestro proceso de adopción</p>
                <button className="mt-2 bg-white/50 rounded-md px-4 text-gray-500 hover:text-cyan-500 transition-all hover:bg-white">CONOCE MÁS</button>
            </div>

            <div className="w-[250px] h-[250px] rounded-[50%] bg-slate-200 bg-cover bg-bottom overflow-hidden flex flex-col items-center justify-start pt-[2rem]" style={{backgroundImage: `url(${info2.src})`}}>
                <p className="max-w-[20ch] text-center text-sm text-white">¿Tienes alguna duda? escríbenos</p>
                <button className="mt-2 bg-white/50 rounded-md px-4 text-gray-500 hover:text-cyan-500 transition-all hover:bg-white">CONTÁCTANOS</button>
            </div>


        </div>
    </div>
}