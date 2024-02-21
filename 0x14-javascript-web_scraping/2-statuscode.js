#!/usr/bin/node

const request = require('request');

function statusCode (link) {
  request(link, (error, response) => {
    if (error) {
      console.error(error);
    } else { console.log(`code: ${response.statusCode}`); }
  });
}

statusCode(process.argv[2]);
