#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
    const val = dict[key];
    newDict[val] = [];
}
for (const key in dict) {
    const val = dict[key];
    newDict[val].push(key);
}
console.log(newDict);