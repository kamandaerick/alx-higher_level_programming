#!/usr/bin/node
/**
 * Add the first two commandline arguments
 */
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
/**
 *This function adds two arguments
 * @param {int} a first argument
 * @param {int} b second argument
 */
function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(a, b);
