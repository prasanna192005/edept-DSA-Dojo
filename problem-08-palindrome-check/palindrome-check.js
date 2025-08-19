// Problem 08: Palindrome Check
// Edept Dojo
const fs=require("fs"); 
const s=fs.readFileSync(0,"utf-8").trim(); 
console.log(s===s.split("").reverse().join("")?"Yes":"No");
