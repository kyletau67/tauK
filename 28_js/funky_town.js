
function fibbonacci(num){
  var a = 1, b = 0, temp;
  while (num >= 0){
    temp = a;
    a = a + b;
    b = temp;
    num--;
  }
  return b
}

function min(a,b) {
  if (a<=b){
    return a;
  }
  else{
    return b;
  }
}

function gcd(a,b) {
  var d = 1, c = min(a,b), gcd = 0;
  while (d <= c) {
    if ((a % d == 0) && (b % d == 0)){
		    gcd = d; //if both params are divisible by d, gcd is replaced
	    }
	  d += 1; //force is added to d to make it more brute
	}
	return gcd;
}

function randomStudent(){
  var names = ["Kaitlin", "Kyle", "Tim", "Mr. Brown", "Aaron", "Ricky"];
  var x = Math.floor(Math.random(names.length - 1 )*names.length);

  return names[x] + x;
}
