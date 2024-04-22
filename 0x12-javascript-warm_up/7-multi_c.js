#!/usr/bin/node
/**
 * This script checks the argument supplied.
 * if it is an int, it prints 'C if fun' that number of times
 */
const x = Number(process.argv[2]);

if (isNaN(x) || x % 1 !== 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
