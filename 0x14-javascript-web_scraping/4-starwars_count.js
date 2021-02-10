#!/usr/bin/node
//  script that prints the number of movies where the character “Wedge Antilles” is present.
// ID of the character = 18
let counter = 0;
const id = '/18/';
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'; // process.argv[2];
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const numberFilms = JSON.parse(body).count;
  for (let i = 0; i < numberFilms; i++) {
    const characters = JSON.parse(body).results[i].characters;
    characters.forEach(char => {
      // console.log(char);
      if (char.includes(id)) {
        counter += 1;
      }
    });
  }
  console.log(counter);
});
