// Problem 06: Multiplication Table
// Edept Dojo
const fs=require("fs"); 
const n=+fs.readFileSync(0,"utf-8").trim(); 
console.log([...Array(10)].map((_,i)=>n*(i+1)).join(" "));
