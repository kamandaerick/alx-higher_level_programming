#!/usr/bin/node
/**
 * This script prints a square whose size is given as a
 * command line argument
 */
const size = Number(process.argv[2]);

if (isNaN(size) || size % 1 !== 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';

    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
