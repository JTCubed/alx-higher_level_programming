#!/usr/bin/node

const { argv } = require('node:process');

const num = Number(argv[2]);

function factorial (a) {
  if (!a) {
    return 1;
  }
  if (a === 0) {
    return 1;
  } else {
    return (factorial(a - 1) * a);
  }
}

const fac = factorial(num);

console.log(fac);
