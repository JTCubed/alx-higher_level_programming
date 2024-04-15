#!/usr/bin/node

const { argv } = require('node:process');

const firstArg = argv[2];

if (argv[2]) {
  console.log(`${firstArg}`);
} else {
  console.log('No argument');
}
