#!/usr/bin/node
/**
 * Create class Square extending class Rectangle
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
