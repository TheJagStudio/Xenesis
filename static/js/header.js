// Menu Dropdown Code
let mobileMenu = document.querySelector("#mobile-menu");
function toggleMobileMenu() {
	// mobileMenu.classList.toggle('hidden');
	mobileMenu.classList.toggle("left-full");
	mobileMenu.classList.toggle("left-0");
}

// Profile Dropdown Code
let profileDropdownMobile = document.querySelector("#profile-dropdown-mobile");
let profileDropdown = document.querySelector("#profile-dropdown");
function toggleProfileDropdown() {
	// Dropdown for Mobile
	profileDropdownMobile.classList.toggle("h-0");
	profileDropdownMobile.classList.toggle("h-auto");
	profileDropdownMobile.classList.toggle("border");
	profileDropdownMobile.classList.toggle("py-3");
	// Dropdown for Laptop - Tablet
	profileDropdown.classList.toggle("h-0");
	profileDropdown.classList.toggle("h-auto");
	profileDropdown.classList.toggle("border");
	profileDropdown.classList.toggle("py-3");
}

window.addEventListener("scroll", function () {
	const header = document.getElementById("mobile-navbar");
	header.classList.toggle("backdrop-blur-md", window.scrollY > 0);
});
window.addEventListener("scroll", function () {
	const header = document.getElementById("navbar");
	header.classList.toggle("backdrop-blur-md", window.scrollY > 0);
});
