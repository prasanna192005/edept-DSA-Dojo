// Problem 02: Sum of Two
// Edept Dojo
const fs=require("fs"); 
const [a,b]=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number); 
    console.log(a+b);
