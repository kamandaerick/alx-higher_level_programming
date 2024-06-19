#!/usr/bin/node
/**
 * Print the number of arguements already printed
 */
let idx = 0;
exports.logMe = function (item) {
  console.log(`${idx}: ${item}`);
  idx += 1;
};
