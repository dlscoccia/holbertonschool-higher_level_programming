#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length <= 3) {
  console.log('0');
} else {
  const myArray = myArgs.slice(2).sort();
  console.log(myArray[myArray.length - 2]);
}
