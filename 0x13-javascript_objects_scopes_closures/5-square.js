#!/usr/bin/node
/**
 * class Square extends Rectangle
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /**
   * Constructor
   * @param {int} size the size of the square
   */
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
