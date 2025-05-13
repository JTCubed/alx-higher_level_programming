#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    let p = '';

    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (!c) {
          p += 'X';
        } else {
          p += c;
        }
      }
      if (i + 1 < this.size) {
        p += '\n';
      }
    }
    console.log(p);
  }
}

module.exports = Square;
