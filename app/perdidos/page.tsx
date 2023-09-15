import { BiSlider } from 'react-icons/bi';
import { AiOutlinePlus } from 'react-icons/ai';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import Link from 'next/link';
import Card from '@components/page/card';

export default async function page() {

    const datos = await fetch('http://50.18.105.237:5000/api/viewPerdidos/?page=1&size=9')
    .then(response => response.json())
    .then(data => [(data)]);

    const publications = datos[0].items
    const total = datos[0].total
    const page = datos[0].page

    return (
        <div className="pageContainer">

            <div className="container">

                <h1
                    className="text-3xl font-semibold text-gray-700 text-center py-6"
                >
                    Perdidos
                </h1>

                <div className="page-topbar">
                    <div className='flex items-center gap-1'>
                        <button className="btn text-xl font-semibold">
                            <BiSlider className="icon-left" />
                            Filtrar
                        </button>
                        <span className="lbl-results text-sm text-gray-400">{total} Resultados</span>
                    </div>
                    <Link 
                        href="/post"
                        className="btn text-xl font-semibold"
                    >
                        <AiOutlinePlus className="icon-left" />
                        Crear publicación
                    </Link>
                </div>

                <div className='flex flex-row flex-wrap justify-between'>
                    {
                        publications.map(
                            (item: {
                                id: number,
                                publication_date: string,
                                address: string,
                                pet_publication: {
                                    type: string,
                                    name: string,
                                    genre: string,
                                    description: string
                                },
                                image_publication: [
                                    {
                                        url: string
                                    }
                                ]
                            }, index: number) => (
                            <Card 
                                key={index}
                                data={item}
                                link="/perdidos"
                            />
                        ))
                    }
                </div>

            </div>

            <div className='pagination'>
                <a className="btn-pagination active">{page}</a>
                <a className="btn-pagination">2</a>
                <a className="btn-pagination">3</a>
                <a className="btn-pagination">4</a>
                <a className="btn-pagination">5</a>
                <a className="btn-pagination">6</a>
                <a className="btn-pagination gap-1">
                    Siguiente 
                    <FaChevronRight className="icon-right" />    
                </a>
            </div>

        </div>
    )
}