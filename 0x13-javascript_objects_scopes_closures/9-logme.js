#!/usr/bin/node

let o = 0;

exports.logMe = function (item) {
  console.log(`${o}: ${item}`);
  o++;
};
