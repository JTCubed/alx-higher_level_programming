#!/usr/bin/node

const { argv } = require('node:process');

const arr = [];
if (!argv[3]) {
//  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    arr.push(parseInt(argv[i]));
  }
//    console.log(arr.max);
}

function secondH (arr) {
  let max = -Infinity;
  let sec = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      sec = max;
      max = arr[i];
    } else if (arr[i] > sec && arr[i] !== max) {
      sec = arr[i];
    }
  }
  return (sec === -Infinity) ? 0 : sec;
}

console.log(secondH(arr));
