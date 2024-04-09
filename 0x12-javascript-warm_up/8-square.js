#!/usr/bin/node

const { argv } = require('node:process');

const num = Number(argv[2]);

if (num) {
  if (num > 0) {
    let str = '';
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        str += 'X';
      }
      if (i + 1 < num) {
        str += '\n';
      }
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
