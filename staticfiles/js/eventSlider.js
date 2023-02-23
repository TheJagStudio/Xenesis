function handleLeft() {
	let slider = document.getElementById("eventSlider");
	let event = document.getElementById("event");
	slider.scrollLeft += event.offsetWidth + 20;
}
function handleRight() {
	let slider = document.getElementById("eventSlider");
	let event = document.getElementById("event");
	slider.scrollLeft -= event.offsetWidth + 20;
}

// Mouse Drag Script
const slider = document.querySelector(".eventGrabSlider");
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener("mousedown", (e) => {
	isDown = true;
	// slider.classList.add('active');
	startX = e.pageX - slider.offsetLeft;
	scrollLeft = slider.scrollLeft;
});
slider.addEventListener("mouseleave", () => {
	isDown = false;
	slider.classList.remove("active");
});
slider.addEventListener("mouseup", () => {
	isDown = false;
	slider.classList.remove("active");
});
slider.addEventListener("mousemove", (e) => {
	if (!isDown) return;
	e.preventDefault();
	const x = e.pageX - slider.offsetLeft;
	const walk = x - startX; //scroll-fast
	slider.scrollLeft = scrollLeft - walk;
	console.log(walk);
});
