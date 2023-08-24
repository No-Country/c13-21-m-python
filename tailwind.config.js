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
        "maingreen": {
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
        "mainyellow": {
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
        "mainpurple": {
          50: "#F4F0F9",
          100: "#E7DEF2",
          200: "#D2C1E7",
          300: "#BAA0DA",
          400: "#A27FCD",
          500: "#8A5FC0",
          600: "#6E41A5",
          700: "#53317C",
          800: "#382154",
          900: "#1B1028",
          950: "#0F0916"
        }
      }
    },
  },
  plugins: [],
}
