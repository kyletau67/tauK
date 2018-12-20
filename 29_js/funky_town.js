//Team OK -- Ahnaf Kazi & Kyle Tau
//SoftDev pd06
//K#29 -- Sequential Progression II: Electric Boogaloo
//2018-12-19

var fibonacci = (n) => {

    if (n == 0) { //base case
        return 0;
    }
    if (n == 1){ //the 1th number is 1 so 1+0 = 1
        return 1;
    }
    else { //all other cases
        return fibonacci(n-2) + fibonacci(n - 1); //adds number and the one before it
    }
};

var gcd = ( a , b ) => {

    var result = 1; //placeholder for gcd

    for (var i = 1; (i <= a) && (i <= b); ++i ) { //starts from smallest number

        if ((a % i == 0) && (b % i == 0)) { //checks if both numbers are divisible by the possible gcd

            result = i; //if so, sets the result variable to the number

        }

    }
    return result; //returns the gcd

};

var randomStudent = () => {

    var students = ['Tim', 'John', 'Steven', 'Damian', 'Shin', 'Vincent', 'Ahnaf', 'Britni'];
    //array holding the students' names
    var amount = students.length;
    //variable holding the size of the array
    var random = Math.random();
    //for convenience

    var student = students[Math.floor( random * amount )];
    //random function takes place and student is chosen
    console.log(student); //log to the console
    return student;
    //chosen student is returned

};

var fibbonaciGo = () => {
    console.log(fibonacci(4)) //log to the console
    return fibonacci(4);
};

var gcdGo = () => {
    console.log(gcd(2,4)); //log to the console
    return gcd(2,4);
};

var fibbut = document.getElementById("fib");
var gcdbut = document.getElementById("gcd");
var stubut = document.getElementById("stu");
var test = document.getElementById("button");
fibbut.addEventListener('click', fibbonaciGo);
gcdbut.addEventListener('click', gcdGo);
stubut.addEventListener('click', randomStudent);
//randomstudent doesn't need a parameter
