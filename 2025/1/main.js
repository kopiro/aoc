const { log, count } = require("console");
const fs = require("fs");

function puzzleOne(lines) {
  let position = 50;
  let countZero = 0;
  lines.forEach((line) => {
    let positionBefore = position;
    const direction = line[0];
    const number = Number(line.substr(1));
    if (direction === "L") {
      position = (position - number) % 100;
    } else if (direction === "R") {
      position = (position + number) % 100;
    }
    if (position < 0) {
      position = 100 + position;
    }
    if (position === 0) {
      countZero++;
    }
  });
  return countZero;
}

function puzzleTwo(lines) {
  let position = 50;
  let countZero = 0;
  let countZeroPrev = 0;

  lines.forEach((line) => {
    let positionBefore = position;
    let zeroToAdd = 0;
    const direction = line[0];
    const number = Number(line.substr(1));
    if (direction === "L") {
      position = position - number;
    } else if (direction === "R") {
      position = position + number;
    }

    if (position < 0) {
      let rotations = Math.ceil(Math.abs(position) / 100);
      if (positionBefore === 0 && Math.abs(position) % 100 !== 0) {
        rotations--;
        rotations = Math.max(0, rotations);
      }
      if (position % 100 === 0) {
        rotations++;
      }
      zeroToAdd = rotations;
      //   console.log(rotations);
      countZero = countZero + zeroToAdd;
      // ---
      position = (1 + rotations) * 100 + position;
    } else if (position >= 100) {
      const rotations = Math.floor(position / 100);

      //   console.log(rotations);
      zeroToAdd = rotations;
      countZero = countZero + zeroToAdd;
      // ---
    } else if (position === 0) {
      zeroToAdd = 1;
      countZero = countZero + zeroToAdd;
    }

    console.log(
      positionBefore,
      "->",
      line,
      "->",
      position,
      "( real ",
      position % 100,
      ") = (",
      zeroToAdd,
      ")"
    );
    position = position % 100;

    // if (position === 0) {
    //   countZeroPrev++;
    // }
  });
  console.log("countZeroPrev", countZeroPrev);
  return countZero;
}

const lines = fs.readFileSync("input.txt").toString().split("\n");
// console.log("Puzzle one: " + puzzleOne(lines));
console.log("Puzzle two: " + puzzleTwo(lines));
