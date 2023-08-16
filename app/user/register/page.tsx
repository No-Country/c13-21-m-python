"use client";

import { useEffect, useState } from "react"
import axios from "axios";

export default function Register() {

    const [state, setState] = useState({
        correo: "",
        password: "",
        repassword: "",
        error: false,
        errorMessage: "",
        success: false,
        successMessage: ""
    })

    const handleChange = (e: any) => {
        const { name, value } = e.target;
        setState({ ...state, [name]: value });
    }

    const handleSubmit = async (e: any) => {

        e.preventDefault();

        if( !state.correo || !state.password || !state.repassword ){
            setState({ ...state, error: true, errorMessage: "Todos los campos son obligatorios!" });
        } 

        if( state.password !== state.repassword ){
            setState({ ...state, error: true, errorMessage: "Las contraseñas no coinciden!" });
        }

        const resp = await axios.post("/api/user", state);
        console.log(resp.data);
    }

    return <div className="w-[100%] h-[100vh] flex flex-col items-center justify-center ">
        <form 
            className="p-4 bg-slate-400 w-[40%] flex flex-col gap-3 align-middle justify-center rounded-md shadow-md"
            onSubmit={handleSubmit}
        >

            { state.error && <div className="bg-red-500 text-white p-2 rounded-md"> { state.errorMessage } </div>}

            <input 
                type="text" 
                name="correo"
                placeholder="Correo" 
                value={state.correo} 
                onChange={handleChange}
            />

            <input 
                type="password" 
                name="password"
                placeholder="Password" 
                value={state.password} 
                onChange={handleChange}    
            />

            <input 
                type="password" 
                name="repassword"
                placeholder="Confirm Password" 
                value={state.repassword}
                onChange={handleChange}
            />
            <button type="submit">Register</button>
        </form>
    </div>
}