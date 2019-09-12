//Function To Display Popup
function newrestaurant_show() {
  document.getElementById("newrestdiv").style.display = "block";
}
//Function to Hide Popup
function newrestaurant_hide() {
  document.getElementById("newrestdiv").style.display = "none";
}
//Function To Display Popup
function editrestaurantname_show() {
  document.getElementById("editrestdiv").style.display = "block";
}
//Function to Hide Popup
function editrestaurantname_hide() {
  document.getElementById("editrestdiv").style.display = "none";
}
//Function To Display Popup
function deleterestaurant_show() {
  document.getElementById("deleterestdiv").style.display = "block";
}
//Function to Hide Popup
function deleterestaurant_hide() {
  document.getElementById("deleterestdiv").style.display = "none";
}
//Function to display edit/delete restaurants
function editrestaurant_show() {
  var x = document.getElementsByClassName("editmenubuttons");
  for (i = 0; i < x.length; i++) {
    if ((x.item(i).style.display == "none") | (x.item(i).style.display == "")) {
      x.item(i).style.display = "grid";
    } else {
      x.item(i).style.display = "none";
    }
  }
}
