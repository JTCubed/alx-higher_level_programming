#!/usr/bin/node

const { argv } = require('node:process');

const num = argv[2];

const conv = Number(num);

if (!conv) {
  console.log('Not a number');
} else {
  console.log(`My number: ${conv}`);
}
