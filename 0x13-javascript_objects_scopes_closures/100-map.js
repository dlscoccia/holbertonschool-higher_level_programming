#!/usr/bin/node
const list = require('./100-data.js').list;
const mapList = list.map((x, index) => x * index);
console.log(list);
console.log(mapList);
