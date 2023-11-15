#!/usr/bin/node
/**
 * This script executes a function a number of times
 * @param {int} x the number of times to call the function
 * @param {Function} theFunction the function to call
 */
function myFunc (x, theFunction) {
  if (x <= 0) {
    return;
  }
  theFunction();
  myFunc(x - 1, theFunction);
}
module.exports = {
  myFunc
};
