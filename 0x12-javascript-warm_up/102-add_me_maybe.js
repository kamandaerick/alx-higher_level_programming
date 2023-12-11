#!/usr/bin/node
/**
 * @param {int} number the number to update
 * @param {Function} theFunction the function to call
 */
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}
module.exports = {
  addMeMaybe
};
