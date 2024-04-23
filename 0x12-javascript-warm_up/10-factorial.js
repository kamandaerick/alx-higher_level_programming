#!/usr/bin/node

const n = parseInt(process.argv[2]);
let factorial = 1;

if (isNaN(n)) factorial = 1;

for (let i = 1; i <= n; i++) {
  factorial = factorial * i;
}
console.log(factorial);
