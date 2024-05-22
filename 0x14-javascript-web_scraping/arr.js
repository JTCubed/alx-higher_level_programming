#!/usr/bin/node

let arr = [];

for (i = 0; i < 10; i++) {
    let j = i;
    arr[j.toString()] = i;
}

console.log(arr);
