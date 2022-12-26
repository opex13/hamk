/* eka versio, raaka toimimaton js

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
*/

// Jonin ja Mikan vinkki:
$(”.menu-item”).on(”hover”, function(){
    //Kun hoveratan niin mitä sille tapahtuu, esim:
    $(”.menu-item”).removeClass(“active”); //poistetaan kaikilta
    $(this).addClass(”active”); //lisätään hoveratulle
});
