// run this in the terminal with: node app.js


const express = require("express");
const app = express();


app.get("/", (req, res) => {
  res.send("This is home");
});

app.get("/nothome", (req, res) => {
  console.log("Someone made a request to /nothome")
  res.send("This is not home");
});


//listen for requests
const PORT = 3030;
app.listen(PORT, () => {console.log(`Server started on port ${PORT}`)});