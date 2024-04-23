#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
if (isNaN(n)) {
  console.log(1);
} else {
  const result = factorial(n);
  console.log(result);
}
