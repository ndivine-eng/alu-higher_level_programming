#!/usr/bin/node
const scrpt = process.argv.slice(2);

if (scrpt.length === 0) {
  console.log('No argument');
} else if (scrpt.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
