#!/usr/bin/node
const mySize = parseInt(process.argv[2]);
let result = 1;

if (process.argv.length < 3) {
  console.log('1');
} else {
function factorial (size) {
  if (size === 1) {
    console.log(result);
  } else {
    result *= size;
    size -= 1;
    factorial(size);
  }
}
factorial(mySize);
}