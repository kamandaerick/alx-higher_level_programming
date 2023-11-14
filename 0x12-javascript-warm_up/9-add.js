#!/usr/bin/node
/**
 * Add the first two commandline arguments
 */
const f = Number(process.argv[2]);
const s = Number(process.argv[3]);
/**
 *This function adds two arguments
 * @param {int} a first argument
 * @param {int} b second argument
 */
function add (a, b) {
  const result = a + b;
  return result;
}
// call the function
const x = add(f, s);
console.log(x);
