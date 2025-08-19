// Problem 04: Even or Odd
// Edept Dojo
const fs=require("fs"); 
const n=+fs.readFileSync(0,"utf-8").trim(); 
console.log(n%2===0?"Even":"Odd");
