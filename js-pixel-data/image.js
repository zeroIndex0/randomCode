// import the image and the canvas then get all the pixel data and do stuff with it


let img = document.getElementById("anImage");
console.log(img.width);

let canvas = document.getElementById("myCanvas");
let differentCanvas = document.getElementById("myOtherCanvas")
let anotherCanvas = document.getElementById("myOtherOtherCanvas")
let againAnotherCanvas = document.getElementById("myOtherOtherOtherCanvas")
console.log("Canvas H:", canvas.height, "Canvas W:", canvas.width);

let ctx = canvas.getContext("2d");
let differentCTX = differentCanvas.getContext("2d");
let anotherCTX = anotherCanvas.getContext("2d");
let againAnotherCTX = againAnotherCanvas.getContext("2d");

let particles = [];


function draw() {
  canvas.height = img.height;
  canvas.width = img.width;
  ctx.drawImage(img, 0, 0, img.width, img.height);
  let data = ctx.getImageData(0, 0, img.width, img.height);
  console.log("data length:", data.data.length, "data height:", data.height, "data width", data.width);
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  let particle = {};
  particles.length = 0;

  for (let y = 0; y < data.height; y++) {
    for (let x = 0; x < data.width; x++) {
      let p = (x + y * data.width) * 4;
      particle = {
        x: x,
        y: y,
        red: data.data[p],
        green: data.data[p + 1],
        blue: data.data[p + 2],
        alpha: data.data[p + 3],
      }
      particles.push(particle);
    }
  }
  render();
}

const render = () => {
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  console.log(particles.length);
  for (let i = 0; i < particles.length; i++) {
    // console.log("r:", particles[i].red, "g:", particles[i].green, "b:", particles[i].blue);
    ctx.fillStyle = `rgba(
      ${particles[i].red}, 
      ${particles[i].green},
      ${particles[i].blue},
      ${particles[i].alpha})`;
    ctx.fillRect(particles[i].x, particles[i].y, 2, 2);
  }
}



function differentDraw() {
  differentCanvas.height = img.height;
  differentCanvas.width = img.width;
  ctx.drawImage(img, 0, 0, img.width, img.height);
  let data = ctx.getImageData(0, 0, img.width, img.height);
  // differentCTX.clearRect(0, 0, canvas.width, canvas.height);
  let particle = {};
  particles.length = 0;

  for (let y = 0; y < data.height; y++) {
    for (let x = 0; x < data.width; x++) {
      let p = (x + y * data.width) * 4;
      if (data.data[p] > 20 && data.data[p] < 128) {
        particle = {
          x: x,
          y: y,
          color: "#080838",
        }
        particles.push(particle);
      } else if (data.data[p] < 170) {
        particle = {
          x: x,
          y: y,
          color: "#898989",
        }
        particles.push(particle);
      } else if (data.data[p] < 160) {
        particle = {
          x: x,
          y: y,
          color: "#d0430b",
        }
        particles.push(particle);
      } else if (data.data[p] >= 160) {
        particle = {
          x: x,
          y: y,
          color: "#F5CCB0",
        }
        particles.push(particle);
      }
    }
  }
  differentRender();
}

const differentRender = () => {
  // differentCTX.clearRect(0, 0, canvas.width, canvas.height);
  console.log(particles.length);
  for (let i = 0; i < particles.length; i++) {
    differentCTX.fillStyle = particles[i].color;
    differentCTX.fillRect(particles[i].x, particles[i].y, 2, 2);
  }
}



function anotherDraw() {
  anotherCanvas.height = img.height;
  anotherCanvas.width = img.width;
  ctx.drawImage(img, 0, 0, img.width, img.height);
  let data = ctx.getImageData(0, 0, img.width, img.height);
  // anotherCTX.clearRect(0, 0, canvas.width, canvas.height);
  let particle = {};
  particles.length = 0;

  for (let y = 0; y < data.height; y++) {
    for (let x = 0; x < data.width; x++) {
      let p = (x + y * data.width) * 4;
      particle = {
        x: x,
        y: y,
        red: 255 - data.data[p],
        green: 255 - data.data[p + 1],
        blue: 255 - data.data[p + 2],
        alpha: data.data[p + 3],
      }
      particles.push(particle);
    }
  }
  anotherRender();
}

const anotherRender = () => {
  // anotherCTX.clearRect(0, 0, canvas.width, canvas.height);
  console.log(particles.length);
  for (let i = 0; i < particles.length; i++) {
    // anotherCTX.fillStyle = particles[i].color;
    anotherCTX.fillStyle = `rgba(
      ${particles[i].red}, 
      ${particles[i].green},
      ${particles[i].blue},
      ${particles[i].alpha})`;
    anotherCTX.fillRect(particles[i].x, particles[i].y, 2, 2);
  }
}



// ==================================== WIP ================================================== \\
//in my render function is where im trying to do the dither stuff, thats not going to work
//I need to do my dither stuff right here, but im a bit unsure of adding my pixels to the particle object
//since ill be looping back over them and just restting them.  Its something i have to think about
//it might not be the case but most likey thats going to be an issue of just rewriting over everyting ive already done.
// function againAnotherDraw() {
//   againAnotherCanvas.height = img.height;
//   againAnotherCanvas.width = img.width;
//   ctx.drawImage(img, 0, 0, img.width, img.height);
//   let data = ctx.getImageData(0, 0, img.width, img.height);
//   // againAnotherCTX.clearRect(0, 0, canvas.width, canvas.height);
//   let particle = {};
//   particles.length = 0;
//   let factor = 1;

//   for (let y = 0; y < data.height; y++) {
//     for (let x = 0; x < data.width; x++) {
//       let p = (x + y * data.width) * 4;
//       particle = {
//         x: x,
//         y: y,
//         red: Math.round(factor * data.data[p] / 255) * (255 / factor),
//         green: Math.round(factor * data.data[p + 1] / 255) * (255 / factor),
//         blue: Math.round(factor * data.data[p + 2] / 255) * (255 / factor),
//         alpha: data.data[p + 3],
//         errorRed: data.data[p] - Math.round(factor * data.data[p] / 255) * (255 / factor),
//         errorGreen: data.data[p + 1] - Math.round(factor * data.data[p + 1] / 255) * (255 / factor),
//         errorBlue: data.data[p + 2] - Math.round(factor * data.data[p + 2] / 255) * (255 / factor),
//       }
//       particles.push(particle);
//     }
//   }
//   againAnotherRender();
// }

// const againAnotherRender = () => {
//   // againAnotherCTX.clearRect(0, 0, canvas.width, canvas.height);
//   console.log(particles.length);
//   for (let i = 1; i < particles.length; i++) {
//     // againAnotherCTX.fillStyle = particles[i].color;
//     let red = particles[i].red;
//     let green = particles[i].green;
//     let blue = particles[i].blue;
//     againAnotherCTX.fillStyle = `rgba(
//       ${red}, 
//       ${green},
//       ${blue},
//       ${particles[i].alpha})`;
//     againAnotherCTX.fillRect(particles[i].x, particles[i].y, 2, 2);

//     red = particles[i].red + particles[i].errorRed * 7/16;
//     green = particles[i].green + particles[i].errorGreen * 7/16;
//     blue = particles[i].blue + particles[i].errorBlue * 7/16;
//     againAnotherCTX.fillStyle = `rgba(
//       ${red}, 
//       ${green},
//       ${blue},
//       ${particles[i].alpha})`;
//     againAnotherCTX.fillRect(particles[i].x+1, particles[i].y, 2, 2);

//     red = particles[i].red + particles[i].errorRed * 3/16;
//     green = particles[i].green + particles[i].errorGreen * 3/16;
//     blue = particles[i].blue + particles[i].errorBlue * 3/16;
//     againAnotherCTX.fillStyle = `rgba(
//       ${red}, 
//       ${green},
//       ${blue},
//       ${particles[i].alpha})`;
//     againAnotherCTX.fillRect(particles[i].x-1, particles[i].y+1, 2, 2);

//     red = particles[i].red + particles[i].errorRed * 5/16;
//     green = particles[i].green + particles[i].errorGreen * 5/16;
//     blue = particles[i].blue + particles[i].errorBlue * 5/16;
//     againAnotherCTX.fillStyle = `rgba(
//       ${red}, 
//       ${green},
//       ${blue},
//       ${particles[i].alpha})`;
//     againAnotherCTX.fillRect(particles[i].x, particles[i].y+1, 2, 2);

//     red = particles[i].red + particles[i].errorRed * 1/16;
//     green = particles[i].green + particles[i].errorGreen * 1/16;
//     blue = particles[i].blue + particles[i].errorBlue * 1/16;
//     againAnotherCTX.fillStyle = `rgba(
//       ${red}, 
//       ${green},
//       ${blue},
//       ${particles[i].alpha})`;
//     againAnotherCTX.fillRect(particles[i].x+1, particles[i].y+1, 2, 2);
//   }
// }

img.onload = drawPage();

function drawPage() {
  draw();
  differentDraw();
  anotherDraw();
  // againAnotherDraw();  //WIP
  //hide the real image after everything is finished
  img.style.display = "none";
}

