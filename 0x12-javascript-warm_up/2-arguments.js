#!/usr/bin/node

const { argv } = require('node:process');

if (!argv[2]) {
  console.log('No argument');
} else if (argv[2] && !argv[3]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
