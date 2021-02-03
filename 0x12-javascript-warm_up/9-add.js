#!/usr/bin/node
function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  return (result);
}
console.log(add(process.argv[2], process.argv[3]));
