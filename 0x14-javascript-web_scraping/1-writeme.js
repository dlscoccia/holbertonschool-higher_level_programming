#!/usr/bin/node

let fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs = require('fs');
fs.writeFile(file, content, function (err) {
  if (err) return console.log(err);
  console.log(`${content} > ${file}`);
});
