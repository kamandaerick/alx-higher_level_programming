#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

if (process.argv.length < 2) {
  console.log('NaN');
} else {
  function add (a, b) {
    const sum = a + b;
    console.log(sum);
  }
  add(first, second);
}
