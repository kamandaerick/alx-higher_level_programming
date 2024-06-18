#!/usr/bin/node
/**
 * Find the factorial of a number
 */
const a = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 0) {
    return 1;
  }
  if (isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(a));
