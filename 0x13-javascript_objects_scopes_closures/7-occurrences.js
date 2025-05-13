#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let o = 0;

  for (const i in list) {
    // console.log(list[i]);
    if (list[i] === searchElement) {
      o++;
    }
  }
  return o;
};
