#!/usr/bin/node
/**
 * Create an emty object if the dimensions are 0 or negative
 */
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
      this.emptyObject = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
