#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/**
 * class Square extends Rectangle
 */

class Square extends Rectangle {
  /**
   * Constructor for the class Square
   * @param {int} size the size of the square
   */
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;
