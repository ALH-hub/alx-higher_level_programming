#!/usr/bin/node

const request = require('request');

function getMovie (movieUrl) {
  request(movieUrl, { encoding: 'utf-8' }, (error, response, body) => {
    if (!error) {
      const results = JSON.parse(body).results;
      console.log(results.reduce((count, movie) => {
        return movie.character.find((character) => character.endsWith('/18'))
          ? count + 1
          : count;
      }, 0));
    }
  });
}

getMovie(process.argv[2]);
