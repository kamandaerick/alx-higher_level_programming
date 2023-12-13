#!/usr/bin/node
/**
 * Return a list in reverse
 * @param {list} list  a list of data
 * @returns a reversed list
 */
exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
