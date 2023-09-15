'use client';

import { useRouter } from 'next/navigation';
import { FaChevronLeft } from 'react-icons/fa';

import MyMap from '../components/page/map';


export default function Page() {

    const router = useRouter();

    return <div className="pageContainer">

            <div className="container">

                <h1
                    className="text-3xl font-semibold text-gray-700 text-center py-6"
                >
                    Crear publicación
                </h1>


                <div className="page-topbar duration-1000 ">
                    <div className='flex items-center gap-1'>
                        <button 
                            className="btn text-xl font-semibold"
                            onClick={() => router.back()}     
                        >
                            <FaChevronLeft /> Volver
                        </button>
                    </div>
                </div>

                <div className="postForm flex my-16">

                    <h4>Fotos</h4>

                    <div className='pics-section'>
                        <div className='pics'>
                            <div className='pic-container'></div>
                            <p>Subir fotos. Tamaño máximo 2MB.</p>
                        </div>
                        <button className='btn-purple mr-4'>Buscar</button>
                    </div>

                    <div className='wrap-group'>

                        <div className='form-group-3 mr-[1rem]'>
                            <label htmlFor="pet-name">Nombre de la mascota</label>
                            <input type="text" name='pet-name' placeholder='Ej. Margarita'/>
                        </div>

                        <div className='form-group-3 mx-[1rem]'>
                            <label htmlFor="species">Especie</label>
                            <select name="speciees">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> Perro </option>
                                <option value="2"> Gato </option>
                            </select>
                        </div>

                        <div className='form-group-3 ml-[1rem]'>
                            <label htmlFor="gender">Sexo</label>
                            <select name="gender">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> Macho </option>
                                <option value="2"> Hembra </option>
                                <option value="3"> Elicoptero apache </option>
                            </select>
                        </div>

                    </div>

                    <div className='wrap-group'>

                        <div className='form-group-1'>
                            <label htmlFor="city">Ciudad</label>
                            <input type="text" name='city' placeholder='Ej: Castelar'/>
                        </div>

                    </div>

                    <h4>Datos de contacto</h4>

                    <div className='wrap-group'>

                        <div className='form-group-3 mr-[1rem]'>
                            <label htmlFor="name">Nombre</label>
                            <input type="text" name='name' placeholder='Ej. Martha'/>
                        </div>

                        <div className='form-group-3 mx-[1rem]'>
                            <label htmlFor="phone">Tel&eacute;fono</label>
                            <input type="text" name='phone' placeholder='Ej: 1165849839'/>
                        </div>


                        <div className='form-group-3'></div>

                    </div>

                    <h4>Datos de contacto</h4>

                    <div className='wrap-group'>

                        <div className='form-group-3 mr-[1rem]'>
                            <label htmlFor="fur">Pelaje</label>
                            <select name="fur">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> A </option>
                                <option value="2"> B </option>
                                <option value="3"> C </option>
                            </select>
                        </div>

                        <div className='form-group-3 mx-[1rem]'>
                            <label htmlFor="color">Color</label>
                            <select name="color">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> A </option>
                                <option value="2"> B </option>
                                <option value="3"> C </option>
                            </select>
                        </div>

                        <div className='form-group-3 ml-[1rem]'>
                            <label htmlFor="size">Tamaño</label>
                            <select name="size">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> A </option>
                                <option value="2"> B </option>
                                <option value="3"> C </option>
                            </select>
                        </div>

                    </div>


                    <div className='wrap-group'>

                        <div className='form-group-3 mr-[1rem]'>
                            <label htmlFor="eyes">Color de ojos</label>
                            <select name="eyes">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> A </option>
                                <option value="2"> B </option>
                                <option value="3"> C </option>
                            </select>
                        </div>

                        <div className='form-group-3 mx-[1rem]'>
                            <label htmlFor="age">Edad</label>
                            <select name="age">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> A </option>
                                <option value="2"> B </option>
                                <option value="3"> C </option>
                            </select>
                        </div>

                        <div className='form-group-3 ml-[1rem]'>
                            <label htmlFor="tag">Tiene collar?</label>
                            <select name="tag">
                                <option value="0"> Seleccionar </option>
                                <option value="1"> A </option>
                                <option value="2"> B </option>
                                <option value="3"> C </option>
                            </select>
                        </div>

                    </div>

                    <div className='wrap-group'>
                        <div className='form-group-1'>
                            <label htmlFor="description">Descripción</label>
                            <textarea name="description"></textarea>
                        </div>
                    </div>

                    <h4>Visto por última vez</h4>
                    <div className='rounded-lg overflow-hidden'>
                        <MyMap />
                    </div>

                    <div className='mt-4 flex items-center justify-end gap-2'>
                        <button className='btn-purple-outline'>Cancelar</button>
                        <button className='btn-purple'>Guardar y revisar</button>
                    </div>


                </div>
            </div>
        </div>
}