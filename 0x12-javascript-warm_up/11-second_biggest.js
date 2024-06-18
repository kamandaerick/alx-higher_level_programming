#!/usr/bin/node
/**
 * This script prints the second largest number in an array
 */
for (let i = 2; i < process.argv.length; i++) {
  process.argv[i] = Number(process.argv[i]);
}

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(arg => parseInt(arg));
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
