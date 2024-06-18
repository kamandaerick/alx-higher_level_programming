#!/usr/bin/node
/**
 * This script iterates and prints items of an array
 * using a for in loop
 */
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (const i in arr) {
  console.log(arr[i]);
}
