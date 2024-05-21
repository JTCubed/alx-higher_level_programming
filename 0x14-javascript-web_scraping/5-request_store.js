#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');
const request = require('request');

const url = argv[2];
const file = argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const contents = (body);
  fs.writeFile(file, contents, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
