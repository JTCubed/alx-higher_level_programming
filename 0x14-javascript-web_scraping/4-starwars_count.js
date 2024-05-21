#!/usr/bin/node

const { argv } = require('node:process');
const url = argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body);
  const perurl = 'https://swapi-api.alx-tools.com/api/people/18/';
  let num = 0;
  for (const fi of films.results) {
  // console.log(fi["characters"]);
    for (const char18 of fi.characters) {
      if (char18 === perurl) {
        num++;
      }
    }
  }
  console.log(num);
});
