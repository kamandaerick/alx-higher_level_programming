#!/usr/bin/node
/**
 * Increment a number and call a function
 * @param {int} number the number to update
 * @param {Function} theFunction the function to call
 */
function addMeMaybe (number, theFunction) {
  const newNumber = number + 1;
  theFunction(newNumber);
}
module.exports = {
  addMeMaybe
};
