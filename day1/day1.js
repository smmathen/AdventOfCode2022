const fs = require("fs");

const vals = fs.readFileSync("input.txt", { encoding: "utf-8" }).trim().split("\n");

// console.log(vals);
let totals = [];
let temp_total = 0;
for (let cals of vals) {
    if (cals.length === 0) {
        totals.push(temp_total);
        temp_total = 0;
    } else {
        temp_total += parseInt(cals);
    }
}

console.log(totals.sort().reverse().slice(0, 3).reduce((sum, val) => sum + val, 0));