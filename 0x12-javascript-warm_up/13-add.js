#!/usr/bin/node
/**
 * This script declares a global function
 * @param {int} a an integer
 * @param {int} b an integer
 * @returns an integer (sum of a and b)
 */
const add = function (a, b) {
  return a + b;
};
module.exports = {
  add
};
