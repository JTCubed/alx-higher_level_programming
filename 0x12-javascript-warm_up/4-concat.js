#!/usr/bin/node

const { argv } = require('node:process');

const sent = `${argv[2]} ` + 'is' + ` ${argv[3]}`;

console.log(sent);
