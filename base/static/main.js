let search = document.querySelector('.search-box');

document.querySelector('#search-icon').onclick = () => {
    search.classList.toggle('active')
    navbar.classList.remove('active')
}

//navbar

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-icon').onclick = () => {
    navbar.classList.toggle('active')
    search.classList.remove('active')
}

window.onscroll = () => {
    navbar.classList.toggle('active')
    search.classList.remove('active')
}