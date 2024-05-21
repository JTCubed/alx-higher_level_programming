#!/usr/bin/node

const { argv } = require('node:process');
const num = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${num}`;

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonf = JSON.parse(body);
  console.log(jsonf.title);
});
