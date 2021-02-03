#!/usr/bin/node
const argvLen = process.argv;

if (argvLen <= 2) {
  console.log('No argument');
} else {
  console.log(argvLen[2]);
}
