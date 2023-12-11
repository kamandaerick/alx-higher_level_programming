#!/usr/bin/node
/**
 * This script prints the second largest number in an array
 */
const arr = [];
const len = process.argv.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr.push(process.argv[i]);
  }
  /**
   * Sorting function for numbers in the array
   */
  arr.sort(function (a, b) {
    return a - b;
  });
  console.log(arr[arr.length - 2]);
}

