#!/usr/bin/node
const scrpt = process.argv[2];
if (scrpt === undefined) {
  console.log('No argument');
} else {
  console.log(scrpt);
}
