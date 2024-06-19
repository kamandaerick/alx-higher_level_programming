#!/usr/bin/node
/**
 * Check the dimensions of the rectangle
 */

class Rectangle {
  /**
   * Initializes a new instance of the Rectangle class with the
   * specified width and height.
   *
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      this.emptyObject = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
