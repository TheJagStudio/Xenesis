import React from 'react'

const Navbar = () => {
  return (
    <div className='flex items-center fixed w-full z-50 justify-between border-none bg-[#0c0c35] p-4 px-32 before:h-[40px] before:w-56 before:clip-header-line before:absolute before:-bottom-10 before:border-none before:left-0 before:bg-[#0c0c35] before:border-white before:z-50'>
      <div className='w-[140px]'>
        <img src="https://html.dynamiclayers.net/te/galactic/assets/img/logo.png" alt="Xenesis" className='w-full h-full' />
      </div>
      <ul className='flex gap-7'>
        <li className='text-white font-semibold uppercase'>Home</li>
        <li className='text-white font-semibold uppercase'>Events</li>
        <li className='text-white font-semibold uppercase'>About Us</li>
      </ul>
      <button className='bg-[#9740fe] border-none py-1 px-5 leading-10 clip-button transition-all duration-300 hover:-translate-y-1'><a href='' className='w-full h-full text-white bg-transparent'>Register an Event</a></button>
    </div>
  )
}

export default Navbar