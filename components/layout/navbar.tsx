import Link from "next/link";

export default function Navbar() {


  return (
    <div className="w-full shadow-md h-20 lg:h{12vh} sticky top-0 z-50 bg-blue-200 px-4">
      <div className="max-w-container h-full mx-auto py-1 font-titleFont flex items-center justify-between">
        <div className="flex flex-row items-center">
          <Link href="/" className="text-xl font-bold text-slate-700">
            NextJs&FastApi
          </Link>
        </div>
        
        <div className="mdl:inline-flex items-center gap-7 ">
            <Link href="/user/register">Registrarse</Link>
        </div>
      </div>
    </div>
)}