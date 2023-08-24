import { ex1, ex2, ex3 } from "@public/assets"

export default function Exito() {

    const data = [
        {
            name: 'Charlie',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: ex1.src
        },
        {
            name: 'Pony',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: ex2.src
        },
        {
            name: 'Mollete',
            description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl eget aliquam ultricies, nunc nisl aliquet.',
            image: ex3.src
        },
    ]

    return <div className="w-full bg-slate-100 py-32">
        <div className="px-32 text-center">
            <h1 className="text-3xl font-bold text-cyan-500">HISTORIAS DE ÉXITO</h1>
            <div className="flex flex-row justify-center gap-[3rem] mt-6">
            { data.map((d, index) => (
                    <div className="w-[250px] h-[250px] bg-cover bg-center flex items-end justify-center rounded-md" style={{backgroundImage: `url(${d.image})`}}>
                        <div className="mt-2 text-gray-500 bg-white/70 mb-3 px-2 rounded-md">{d.name}</div>
                    </div>
                ))}
            </div>

            <div>
            <button className=" bg-yellow-600 text-white px-4 py-2 rounded-md mt-6">VER MAS</button>
        </div>

        </div>
    </div>
}