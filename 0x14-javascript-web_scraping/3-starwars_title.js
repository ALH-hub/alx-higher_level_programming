#!/usr/bin/node

const request = require('request');

function getMovie (movieId) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(movieUrl, { encoding: 'utf-8' }, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}

getMovie(process.argv[2]);
