#!/usr/bin/node
const myArgs = process.argv.slice(2);
const num = parseInt(myArgs[0]);
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
