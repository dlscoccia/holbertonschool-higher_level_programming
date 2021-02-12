#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const completedDict = {};
let counter = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  let lastUser = '';
  for (let i = 0; i < data.length; i++) {
    if (data[i].userId !== lastUser) {
      counter = 0;
    }
    if (data[i].completed === true) {
      counter += 1;
      completedDict[data[i].userId] = counter;
    }
    lastUser = data[i].userId;
  }
  console.log(completedDict);
});
