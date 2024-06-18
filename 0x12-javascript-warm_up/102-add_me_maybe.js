#!/usr/bin/node
/**
 * increment and call a function
 */
exports.addMeMaybe = function (number, theFunction) {
  number = number + 1;
  theFunction(number);
};
