
/*Date*/
var d = new Date();
var curr_date = d.getDate();
var curr_month = d.getMonth() + 1;
var curr_year = d.getFullYear();

var hour = (curr_date + "." + curr_month + "." + curr_year);

var x = document.getElementsByTagName("time");

for (var i = 0; i < x.length; i++) {
    x[i].innerHTML = hour;
}

function load_data() {
    var xhr = new XMLHttpRequest();

    xhr.open('GET', '/movie/all');

    xhr.send(null);
    alert(xhr.responseText);
    console.log(xhr.getResponseHeader("content-type"));
}
