const fs = require("fs");

function puzzleOne(lines) {}

function puzzleTwo(lines) {}

const file = path.join(__dirname, "example.txt");
const lines = fs.readFileSync(file).toString().split("\n");
console.log("Puzzle one: " + puzzleOne(lines));
// console.log("Puzzle two: " + puzzleTwo());
