// Problem 03: Maximum of Two
// Edept Dojo
const fs=require("fs");
const [a,b]=fs.readFileSync(0,"utf-8").trim().split(/\s+/).map(Number);
console.log(Math.max(a,b));
