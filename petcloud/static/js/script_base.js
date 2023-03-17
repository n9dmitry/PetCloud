

function close_burger() {
    menu_burger = document.getElementsByClassName('menu_burger')[0]
    menu_burger.style.display = 'none'
}

function open_burger() {
    menu_burger = document.getElementsByClassName('menu_burger')[0]
    menu_burger.style.display = 'flex'
}

burger_menu = document.getElementById('close_burger')

burger_menu.onclick = close_burger

document.getElementsByClassName('burger')[0].onclick = open_burger