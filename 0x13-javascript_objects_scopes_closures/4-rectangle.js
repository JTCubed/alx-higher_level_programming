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
      }
      if (i + 1 < this.height) {
        a += '\n';
      }
    }
    console.log(a);
  }

  rotate () {
    const i = this.height;
    this.height = this.width;
    this.width = i;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
