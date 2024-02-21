#!/usr/bin/node

const fs = require('fs');

function readFile (filePath, data) {
  return new Promise((resolve, reject) => {
    fs.writeFile(filePath, data, 'utf-8', (err) => {
      if (err) {
        reject(err);
      }
    });
  });
}

readFile(process.argv[2], process.argv[3])
  .catch(err => {
    console.error(err);
  });
