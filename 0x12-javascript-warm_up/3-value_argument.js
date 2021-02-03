#!/usr/bin/node
const argvLen = process.argv;
if (argvLen[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argvLen[2]);
}
