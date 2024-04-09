#!/usr/bin/node

const { argv } = require('node:process');

const num1 = Number(argv[2]);

const num2 = Number(argv[3]);

function add (a, b) {
  return a + b;
}

const num = add(num1, num2);

console.log(num);
