import React from "react";

const Footer = () => {
	return (
		<>
			<div className="flex justify-around px-32 my-2 mb-8">
				<div className="flex flex-col items-center gap-3">
					<img src="https://html.dynamiclayers.net/te/galactic/assets/img/logo.png" alt="Xenesis" className="w-[140px]" />
					<p className="max-w-[200px] text-center text-gray-300">Epic Events organized for ultimate students!</p>
					<div className="flex items-center justify-center gap-5 mt-3">
						<a href="" className="text-[#9740fe] text-2xl hover:-translate-y-2 hover:text-[#dfc5ff] transition-all duration-300">
							<i className="bi bi-facebook"></i>
						</a>
						<a href="" className="text-[#9740fe] text-2xl hover:-translate-y-2 hover:text-[#dfc5ff] transition-all duration-300">
							<i className="bi bi-twitter"></i>
						</a>
						<a href="" className="text-[#9740fe] text-2xl hover:-translate-y-2 hover:text-[#dfc5ff] transition-all duration-300">
							<i className="bi bi-instagram"></i>
						</a>
						<a href="" className="text-[#9740fe] text-3xl hover:-translate-y-2 hover:text-[#dfc5ff] transition-all duration-300">
							<i className="bi bi-youtube"></i>
						</a>
					</div>
				</div>
				<div className="pt-4">
					<h3 className='font-bold text-white text-xl mb-4 pb-2 relative after:content-"" after:absolute after:left-2 after:bottom-0 after:w-[50%] after:h-[3px] after:bg-[#9704fe]'>Useful Links</h3>
					<div className="flex flex-col text-left text-gray-400 gap-1 pl-2">
						<a href="" className="hover:translate-x-2 hover:text-[#bc85ff] transition-all duration-300">
							Events
						</a>
						<a href="" className="hover:translate-x-2 hover:text-[#bc85ff] transition-all duration-300">
							About Us
						</a>
						<a href="" className="hover:translate-x-2 hover:text-[#bc85ff] transition-all duration-300">
							Register in Event
						</a>
						<a href="" className="hover:translate-x-2 hover:text-[#bc85ff] transition-all duration-300">
							Events
						</a>
					</div>
				</div>
				<div className="pt-4">
					<h3 className='font-bold text-white text-xl mb-4 pb-2 relative after:content-"" after:absolute after:left-2 after:bottom-0 after:w-[50%] after:h-[3px] after:bg-[#9704fe]'>Contact Us</h3>
					<div className="flex flex-col text-left gap-2 text-gray-400 pl-2">
						<div className="flex flex-col group cursor-pointer">
							<p className="text-[#9740fe]">Join Us:</p>
							<p className="text-gray-300 text-sm group-hover:translate-x-2 transition-all duration-300">ldrp@gmail.com</p>
						</div>
						<div className="flex flex-col group cursor-pointer">
							<p className="text-[#9740fe]">Phone:</p>
							<p className="text-gray-300 text-sm group-hover:translate-x-2 transition-all duration-300">+91 786 308 5614</p>
						</div>
					</div>
				</div>
				<div className="pt-4">
					<h3 className='font-bold text-white text-xl mb-5 pb-2 relative after:content-"" after:absolute after:left-0 after:bottom-0 after:w-[50%] after:h-[3px] after:bg-[#9704fe]'>Newsletter Signup</h3>
					<div className="flex flex-col text-left gap-2 text-gray-400">
						<form className="flex flex-col items-start gap-3">
							<input type="email" placeholder="abc@xyz.com" className="px-3 py-2 text-sm outline-none bg-transparent border border-gray-500 rounded" />
							<input type="submit" value="Subscribe" className="uppercase cursor-pointer text-xs px-6 py-3 clip-button text-white font-semibold hover:bg-[black] bg-gradient-to-tr from-[#7815ea] to-[#c595ff] hover:translate-x-1 transition-all duration-300" />
						</form>
					</div>
				</div>
			</div>
			<div className="bg-[#0c0c35] w-fit px-24 pr-36 mb-0 clip-copyrights text-gray-300 font-semibold py-8 text-xl">&copy; 2023 Xenesis All Rights Registered</div>
		</>
	);
};

export default Footer;
