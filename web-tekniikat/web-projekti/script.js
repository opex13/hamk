/* eka versio, raaka toimimaton js

const menu = document.getElementsByClassName("menubar");

Array.from(document.getElementsByClassName("menuItem"))
    .forEach((item, index) => {
        item.onmouseover = () => {
            menu.dataset.activeIndex = index;
            console.log(index)
        }
    });
console.log(menu)
console.log(document.getElementsByClassName("menuItem"))
*/

// Jonin ja Mikan vinkki:
$("menuItem").on("hover", (function(){
    $(this).append($("***"));
    //Kun hoveratan niin mitä sille tapahtuu, esim:
    $("menuItem").removeClass("active"); //poistetaan kaikilta
    $(this).addClass("active"); //lisätään hoveratulle
    
}));
