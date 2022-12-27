// eka versio, raaka toimimaton js
///*
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
//*/

// Jonin ja Mikan vinkki:
/*
$(".menuItem").on("hover", (function(){
    //Kun hoveratan niin mitä sille tapahtuu, esim:
    alert("Text: " + $("test").text());
    $(".menuItem").removeClass("active"); //poistetaan kaikilta
    $(this).addClass("active"); //lisätään hoveratulle
}));

$(".menuItem").mouseenter(function(){
    $(this).addClass("active");
    }
    //function(){
    //$(this).removeClass("active");
    //}
);
*/
$(".menuItem").hover(function () {
    $(this).addClass("active");
}, function () {
    $(this).removeClass("active");
});