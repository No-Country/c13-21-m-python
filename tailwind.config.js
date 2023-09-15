/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
      screens:{
        xs: "320px",
        sm: "375px",
        sml: "500px",
        md: "667px",
        mdl: "768px",
        lg: "960px",
        lgl: "1024px",
        xl: "1280px",
      },
      colors: {
        "color1": {
          50: "#E9F7F4",
          100: "#D2EEE9",
          200: "#A9DFD5",
          300: "#7DCFC0",
          400: "#54C0AC",
          500: "#3A9D8B",
          600: "#2F7F70",
          700: "#225D52",
          800: "#173F38",
          900: "#0B1E1A",
          950: "#060F0D"
        },
        "color2": {
          50: "#FDF7E7",
          100: "#FBEFD0",
          200: "#F7DFA1",
          300: "#F3CF72",
          400: "#F0BF42",
          500: "#ECB016",
          600: "#BD8C0F",
          700: "#8D690C",
          800: "#5E4608",
          900: "#2F2304",
          950: "#181102"
        },
        "color3": {
          50: "#F1E1FF",
          100: "#E3C3FE",
          200: "#C581FD",
          300: "#AA45FC",
          400: "#8C04FB",
          500: "#6A03BF",
          600: "#540297",
          700: "#400273",
          800: "#2A014B",
          900: "#160128",
          950: "#0B0014" 
        }
      },
      backgroundImage: {
        'pic-icon': "url('/assets/images/pic_icon.png')",
      }
    },
  },
  plugins: [
  ],
}
