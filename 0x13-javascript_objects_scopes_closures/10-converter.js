#!/usr/bin/node
/**
 * Convert numbers from base 10 to others
 */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
