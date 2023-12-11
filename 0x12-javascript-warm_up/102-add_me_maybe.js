#!/usr/bin/node
/**
 * @param {int} number the number to update
 * @param {Function} theFunction the function to call
 */
function myFunc (number, theFunction) {
  number += 1;
  theFunction();
}
module.exports = {
  myFunc
};
