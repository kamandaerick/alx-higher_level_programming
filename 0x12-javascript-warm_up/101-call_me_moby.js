#!/usr/bin/node
/**
 * @param {int} x the number of times to call the function
 * @param {Function} theFunction the function to call
 */
function callMeMoby (x, theFunction) {
  if (x <= 0) {
    return;
  }
  theFunction();
  callMeMoby(x - 1, theFunction);
}
module.exports = {
  callMeMoby
};
