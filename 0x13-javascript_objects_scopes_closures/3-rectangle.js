#!/usr/bin/node
/**
 * This script prints a rectangle using "X"
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
}
module.exports = Rectangle;
