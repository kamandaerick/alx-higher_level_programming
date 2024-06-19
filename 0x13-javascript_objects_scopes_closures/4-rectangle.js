#!/usr/bin/node
/**
 * Create an emty object if the dimensions are 0 or negative
 * Create an instance method called print
 */
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);
    if (!isNaN(w) && !isNaN(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      //      let line = '';
      for (let j = 0; j < this.width; j++) {
        //    line += 'X';
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const t = this.width;
    this.width = this.height;
    this.height = t;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
