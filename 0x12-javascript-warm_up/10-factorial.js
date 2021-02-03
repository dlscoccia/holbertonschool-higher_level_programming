#!/usr/bin/node
const mySize = parseInt(process.argv[2]);
let result = 1;
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
