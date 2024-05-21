#!/usr/bin/node

const { argv } = require('node:process');
const request = require("request");

const url = argv[2];

request(url, function(error, response, body) {
    const todos = JSON.parse(body);
    let compl = {
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0,
	'7': 0,
	'8': 0,
	'9': 0,
	'10': 0 };
    for (tod of todos) {
	if (tod["userId"] == 1 && tod["completed"] == true) {
	    compl['1'] += 1;
	}
	if (tod["userId"] == 2 && tod["completed"] == true) {
	    compl['2'] += 1;
	}
	if (tod["userId"] == 3 && tod["completed"] == true) {
	    compl['3'] += 1;
	}
	if (tod["userId"] == 4 && tod["completed"] == true) {
	    compl['4'] += 1;
	}
	if (tod["userId"] == 5 && tod["completed"] == true) {
	    compl['5'] += 1;
	}
	if (tod["userId"] == 6 && tod["completed"] == true) {
	    compl['6'] += 1;
	}
	if (tod["userId"] == 7 && tod["completed"] == true) {
	    compl['7'] += 1;
	}
	if (tod["userId"] == 8 && tod["completed"] == true) {
	    compl['8'] += 1;
	}
	if (tod["userId"] == 9 && tod["completed"] == true) {
	    compl['9'] += 1;
	}
	if (tod["userId"] == 10 && tod["completed"] == true) {
	    compl['10'] += 1;
	}
    }
    console.log(compl);
})
