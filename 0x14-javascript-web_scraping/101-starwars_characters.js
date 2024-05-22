#!/usr/bin/node

const { argv } = require('node:process');
const fnum = argv[2];
const furl = `https://swapi-api.alx-tools.com/api/films/${fnum}`;
const request = require('request');
const fs = require('fs');

request(furl, function (error, response, body) {
    const mtjson = JSON.parse(body);
    const chars = mtjson.characters;
    let arr = {};
    var j = 0;
    for (const ch of chars) {
	request(ch, function (error, response, bdy) {
	    const nme = JSON.parse(bdy);
	    fs.writeFileSync("list.txt", nme.name, 'utf8');
	    console.log(nme.name);
	    arr["name"] = nme.name;
//	    j += 1;
	})
    }
//    console.log(arr);
})
