#!/usr/bin/node
/**
 * This script takes the first commandline argument and
 * checks if it is an int then finds its factorial
 */
let number = Number(process.argv[2]);
/**
 * 
 * @param {int} number the number entered as commandline arg
 * @returns an integer (the result of a factorial)
 */
function factorial(number) {
  if (isNaN(number) || number % 1 !== 0) {
    return 1;
  } else if (number === 0 || number === 1) {
    return 1;
  } else {
    let f = number * factorial(number - 1);
    return f;
  }
}
console.log(factorial(number));