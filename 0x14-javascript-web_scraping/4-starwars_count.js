#!/usr/bin/node

const { argv } = require('node:process');
const url = argv[2];
const request = require("request");

request(url, function(error, response, body) {
    const films = JSON.parse(body);
    const perurl = "https://swapi-api.alx-tools.com/api/people/18/"
    let num = 0;
    for (fi of films["results"]) {
	//	console.log(fi["characters"]);
	for (char18 of fi["characters"]) {
	    if (char18 == perurl) {
		num ++;
	    }
	}
    }
    console.log(num);
});
