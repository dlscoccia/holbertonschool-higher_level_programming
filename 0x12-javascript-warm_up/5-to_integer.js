#!/usr/bin/node
const myNumber = process.argv[2];
if (is(myNumber)) {
    console.log('Not a number');
} else {
    console.log(`My number: ${parseInt(myNumber)}`)
}
