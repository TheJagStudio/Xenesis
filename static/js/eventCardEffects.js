function cardOverlayHandle(id) {
	document.getElementById("cardOverlay" + id).classList.remove("top-full");
	document.getElementById("cardOverlay" + id).classList.add("top-0");
	document.getElementById("blurOverlay" + id).classList.add("blur-lg");
	document.getElementById("cardOverlay" + id + "2").classList.remove("top-full");
	document.getElementById("cardOverlay" + id + "2").classList.add("top-0");
	document.getElementById("blurOverlay" + id + "2").classList.add("blur-lg");
}
function cardOverlayHandleClose(id) {
	document.getElementById("cardOverlay" + id).classList.add("top-full");
	document.getElementById("cardOverlay" + id).classList.remove("top-0");
	document.getElementById("blurOverlay" + id).classList.remove("blur-lg");
	document.getElementById("cardOverlay" + id + "2").classList.add("top-full");
	document.getElementById("cardOverlay" + id + "2").classList.remove("top-0");
	document.getElementById("blurOverlay" + id + "2").classList.remove("blur-lg");
}
function handleLike(id) {
	document.getElementById("likeSVG" + id).classList.toggle("hidden");
	document.getElementById("likeSVG" + id).classList.toggle("opacity-0");
	document.getElementById("likeFillSVG" + id).classList.toggle("hidden");
	document.getElementById("likeFillSVG" + id).classList.toggle("opacity-0");
	document.getElementById("likeSVG" + id + "2").classList.toggle("hidden");
	document.getElementById("likeSVG" + id + "2").classList.toggle("opacity-0");
	document.getElementById("likeFillSVG" + id + "2").classList.toggle("hidden");
	document.getElementById("likeFillSVG" + id + "2").classList.toggle("opacity-0");
}
