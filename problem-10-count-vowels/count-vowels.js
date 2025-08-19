// Problem 10: Count Vowels
// Edept Dojo
const fs=require("fs");
const s=fs.readFileSync(0,"utf-8").trim().toLowerCase();
console.log([...s].filter(ch=>"aeiou".includes(ch)).length);
