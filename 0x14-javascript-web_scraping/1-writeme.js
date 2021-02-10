#!/usr/bin/node

const file = process.argv[2];
const content = process.argv[3];
const fs = require('fs'); // import the fs module
fs.writeFile(file, content, 'utf8', function(err) {
    if (err) return console.log(err);
});