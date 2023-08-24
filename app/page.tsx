import HomeSlider from '@components/home/homeSlider';
import Perdidos from '@components/home/perdidos';
import Encontrados from '@components/home/encontrados';
import Adopciones from '@components/home/adopciones';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center">
      <HomeSlider />
      <Perdidos />
      <Encontrados />
      <Adopciones />
    </main>
  )
}
