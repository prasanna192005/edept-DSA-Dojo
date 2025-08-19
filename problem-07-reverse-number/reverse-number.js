// Problem 07: Reverse Number
// Edept Dojo
const fs=require("fs"); 
let n=fs.readFileSync(0,"utf-8").trim(); 
console.log(n.split("").reverse().join(""));
