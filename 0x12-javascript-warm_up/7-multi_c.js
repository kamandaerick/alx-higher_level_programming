#!/usr/bin/node
/**
 * This script checks the argument supplied.
 * if it is an int, it prints 'C if fun' that number of times
 */
const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
