#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response && response.statusCode);
});
