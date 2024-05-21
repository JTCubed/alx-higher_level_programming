#!/usr/bin/node

const request = require('request');
request('http://www.google.com', function (error, response, body) {
// 3-starwars_title.js  console.error('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
});
