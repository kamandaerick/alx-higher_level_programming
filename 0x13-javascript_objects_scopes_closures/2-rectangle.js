#!/usr/bin/node
/**
 * Check the dimensions of the rectangle
 */

class Rectangle {
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
