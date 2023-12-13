#!/usr/bin/node
/**
 * This module prints the number of arguments already printed and the new argument
 */
let index = 0;
/**
 * @param {item} item argument suplied to the function
 */
exports.logMe = function (item) {
  console.log(index + ': ' + item);
  index += 1;
};
