import { BiSlider } from 'react-icons/bi';
import { AiOutlinePlus } from 'react-icons/ai';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';

import Link from 'next/link';

import { data } from '@utils/data';
import  Card from '@components/page/card';

export default function page() {

    const slicedArr = data.slice(0, 9);

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
                        <span className="lbl-results text-sm text-gray-400">358 Resultados</span>
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
                        slicedArr.map((item, index) => (
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
                <a className="btn-pagination active">1</a>
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