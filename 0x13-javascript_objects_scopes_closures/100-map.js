#!/usr/bin/node

const list = require('./100-data').list;

const newl = list.map((x, y, z) => x * y);

console.log(list);
console.log(newl);
