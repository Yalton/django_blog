// When the user scrolls the page, execute myFunction
window.onscroll = function() { myFunction() };

// Get the topnav
var topnav = document.getElementById("topnav");

// Get the offset position of the topnav
var sticky = topnav.offsetTop;

// Add the sticky class to the topnav when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
    if (window.pageYOffset >= sticky) {
        topnav.classList.add("sticky")
    } else {
        topnav.classList.remove("sticky");
    }
}