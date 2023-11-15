#!/usr/bin/node
/**
 * 
 * @param {int} x the number of times to call the function
 * @param {function} theFunction the function to call
 */
function myFunc (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}

module.exports = {
    myFunc
};
