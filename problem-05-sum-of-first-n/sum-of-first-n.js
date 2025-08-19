// Problem 05: Sum of First N
// Edept Dojo
const fs=require("fs"); 
const n=+fs.readFileSync(0,"utf-8").trim(); 
console.log(n*(n+1)/2);
