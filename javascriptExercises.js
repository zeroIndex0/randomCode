//i cant wait until i read more about api and json and using it to build things
//it's exciting.  Screw the compiled languages of the past, welcome to script world!
// i dont really mean that, i still like you C++


//just messing around to capitalize every word, in this case anything after a space
//can I fake a scope like in C++?  Yup, awesome, good to know
//I also dont even need .charAt, i can just use [index]
{
    var data = "How can mirrors be real if our eyes aren't real";
    var result = ""
    result += data[0].toUpperCase();
    for (var i = 1; i < data.length; i++) {
        if (data[i] === " ") {
            // console.log(data.charAt(i + 1).toUpperCase());
            result += data[i];
            result += data.charAt(i + 1).toUpperCase();
            i++;
        } else {
            result += data[i];
        }
    }
    console.log(result);
}

//A bit tricky because i couldnt figure out how to pass anything in, but turns out
// I just have to use 'this'
//I also dont even need .charAt, i can just use [index]
String.prototype.toJadenCase = function () {
    var result = "";
    result += this.charAt(0).toUpperCase(); //Makes the first char uppercase everytime
    for (var i = 1; i < this.length; i++) {
        if (this[i] === " ") {
            result += this[i];
            result += this.charAt(i + 1).toUpperCase();
            i++;
        } else {
            result += this[i];
        }
    }
    return result;
}

testStr = "Hello there, this is a test!";
console.log(testStr.toJadenCase());
