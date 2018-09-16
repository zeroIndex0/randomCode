//just messing around capitalizing every word, in this case anything after a space
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


//-------------------------------------------------------------------------------------------------------------

//testing for a valid ip.  I could have used regexp for the whole thing, but tried to use as little as possible so i could read
//this later.  Also, I havent tested this against anything crazy, was just messing around with javascript
function isValidIP(input) {
    modifiedInput = input.split(".");
    if(modifiedInput.length != 4) {
        return false;
    }
    for(let i = 0; i < modifiedInput.length; i++) {
        if(modifiedInput[i][0] === '0' && Number(modifiedInput[i]) != 0) {
            return false;
        } else if (modifiedInput[i].match(/^[0-9]+$/) === null) {  //should only be digits
            return false;
        } else if (Number(modifiedInput[i]) > 255 || Number(modifiedInput[i]) < 0) {
            return false;
        }
    }
    return true;
}

//test cases
isValidIP("1.2.3.4 ");
isValidIP("1.2.3.4.5");
isValidIP("84.46.0.95");
