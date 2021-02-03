#!/usr/bin/node
let value = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  value = args[args.length - 2];
}
console.log(value);
