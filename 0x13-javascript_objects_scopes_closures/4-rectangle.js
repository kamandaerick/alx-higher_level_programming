#!/usr/bin/node
/**
 * This script defines a class Rectangle and its methods
 */
class Rectangle {
  /**
   * Check the values of h and w if positive
   * @param {int} w width of a rectangle
   * @param {int} h height of a rectangle
   */
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;
    this.width = w;
    this.height = h;
  }
  /**
   * This method prints a rectanggle
   */

  print () {
    for (let i = 1; i <= this.height; i++) {
      let row = '';
      for (let j = 1; j <= this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
  /**
   * Exchange the width and height of the rectangle
   */

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  /**
   * Double the width and height of the rectangle
   */

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
