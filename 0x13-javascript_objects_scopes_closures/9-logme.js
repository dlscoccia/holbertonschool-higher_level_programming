#!/usr/bin/node
const list = [];
let i = 0;
exports.logMe = function (item) {
  list.push(item);
  for (i; i < list.length; i++) {
    console.log(`${i}: ${list[i]}`);
  }
};
