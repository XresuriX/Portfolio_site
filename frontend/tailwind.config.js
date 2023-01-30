/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,tsx}",
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './styles/**/*.css'
  ],
  theme: {
    extend: {
        colors: {
        cobalt: '#0047AB',
        emerald: '#50C878',
        },
    },
  },
  plugins: [],
}
