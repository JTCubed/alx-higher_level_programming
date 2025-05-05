#!/usr/bin/node

function addMeMaybe (x, p) {
  p(x + 1);
}

module.exports.addMeMaybe = addMeMaybe;
