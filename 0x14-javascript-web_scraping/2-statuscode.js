#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
url = argv[2];

request(url, function (error, response, body) {
    console.log(`code:`, response && response.statusCode);
});
