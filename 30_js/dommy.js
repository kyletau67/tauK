/*
TEAM KAILE
Kyle Tau + Kaitlin Wan
K #30: Sequential Progression III: Season of the Witch
2018-12-20
*/

//we used a value added key to sucess!
var changeHeading = function(e){
  var h = document.getElementById("h");
  h.innerHTML = this.innerHTML;
};

var removeItem = function(e){
  this.remove();
  console.log('removed!!!')
};

var lis = document.getElementsByTagName("li");

var returnHeading = function(e){
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
}

for(var i=0; i<lis.length; i++){
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', returnHeading);
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD!";
  list.appendChild(item);
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', returnHeading);
  item.addEventListener('click', removeItem);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);


var fib = function(n){
  if(n<2){
    return 1;
  }
  else{
    return fib(n - 1) + fib(n-2);
  }
}

var counter = 1;
var addFib = function(e){
  var list = document.getElementById("fiblist");
  var item = document.createElement('li');
  item.innerHTML = "" + fib(counter);
  counter += 1;
  list.appendChild(item);
}

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
