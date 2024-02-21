#!/usr/bin/node

const fs = require('fs');

function readFile (pathToFile) {
  return new Promise((resolve, reject) => {
    fs.readFile(pathToFile, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

readFile(process.argv[2])
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.error(err);
  });
