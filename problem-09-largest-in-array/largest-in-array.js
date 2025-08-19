// Problem 09: Largest in Array
// Edept Dojo
const fs=require("fs"); 
const data=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); 
const n=data[0], arr=data.slice(1); 
console.log(Math.max(...arr));
