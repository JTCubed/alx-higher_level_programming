#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
const numf = argv[2];
const filmurl = `https://swapi-api.alx-tools.com/api/films/${numf}`;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchChars () {
  try {
    const filmr = await requestPromise(filmurl);
    const filmdata = JSON.parse(filmr);
    const chars = filmdata.characters;

    for (const charurl of chars) {
      try {
        const charbody = await requestPromise(charurl);
        const chardata = JSON.parse(charbody);
        console.log(chardata.name);
      } catch (error) {
        // pass
      }
    }
  } catch (error) {
    // pass
  }
}

fetchChars();
