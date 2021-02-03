#!/usr/bin/node
const mySize = process.argv[2];
let i;
if (isNaN(mySize)) {
  console.log('Missing size');
} else {
  for (i = 0; i < mySize; i++) {
    console.log('X'.repeat(mySize));
  }
}
