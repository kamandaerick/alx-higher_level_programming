#!/usr/bin/node
/**
 * Find the number of occurences of an element in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) n += 1;
  }
  return n;
};
