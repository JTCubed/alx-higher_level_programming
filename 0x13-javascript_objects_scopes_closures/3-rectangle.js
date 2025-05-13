#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        a += 'X';
      } if (i + 1 < this.height) {
        a += '\n';
      }
    }
    console.log(a);
  }
}

module.exports = Rectangle;
