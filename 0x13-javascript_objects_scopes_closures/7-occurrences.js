#!/usr/bin/node
/**
 * This function returns the number of occurences of an element
 * in a list
 * @param {list} list A list with elements
 * @param {Element} searchElement An element to search
 * @returns the number of times the element apears
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
