#!/usr/bin/node
/**
 * Define and export a class Rectangle with constructor taking 2 arguments
 */
class Rectangle {
  /**
   * @param {int} w width of a rectangle
   * @param {int} h height of a rectangle
   */
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
