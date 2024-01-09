#!/usr/bin/node

const num = Number(process.argv[2]);

if (num) {
  for (let i = 1; i <= num; i++) {
    let row = '';
    for (let j = 1; j <= num; j++) row += 'X';
    console.log(row);
  }
} else {
  console.log('Missing size');
}
