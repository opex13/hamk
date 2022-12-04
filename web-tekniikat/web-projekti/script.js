const menu = document.getElementsByClassName("menubar");

Array.from(document.getElementsByClassName("menu-item"))
    .forEach((item, index) => {
        item.onmouseover = () => {
            menu.dataset.activeIndex = index;
            console.log(index)
        }
    });
console.log(menu)
console.log(document.getElementsByClassName("menu-item"))
