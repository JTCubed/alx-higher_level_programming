#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
const numf = argv[2];
const filmurl = `https://swapi-api.alx-tools.com/api/films/${numf}`;

request(filmurl, function (error, response, body) {
  if (error) {
    // pass
  }
  const tojson = JSON.parse(body);
  const chars = tojson.characters;

  for (const i of chars) {
    request(i, function (error, response, bdy) {
      if (error) {
        // pass
      }
      const charjson = JSON.parse(bdy);
      console.log(charjson.name);
    });
  }
});
