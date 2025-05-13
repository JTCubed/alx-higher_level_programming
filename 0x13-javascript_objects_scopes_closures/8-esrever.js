#!/usr/bin/node

exports.esrever = function (list) {
  const l = [];
  const length = list.length;

  for (let i = length - 1; i >= 0; i--) {
    l.push(list[i]);
  }
  return l;
};
