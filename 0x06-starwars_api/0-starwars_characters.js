#!/usr/bin/node

const https = require('https');

function printMovieCharacters(movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}`;

  https.get(movieUrl, (response) => {
    if (response.statusCode !== 200) {
      console.error(`Error: Status code ${response.statusCode}`);
      return;
    }

    response.on('data', (data) => {
      const movieData = JSON.parse(data);
      const characters = movieData.characters;

      characters.forEach((characterUrl) => {
        https.get(characterUrl, (response) => {
          if (response.statusCode !== 200) {
            console.error(`Error: Status code ${response.statusCode}`);
            return;
          }

          response.on('data', (data) => {
            const characterData = JSON.parse(data);
            console.log(characterData.name);
          });
        });
      });
    });
  });
}

const movieId = parseInt(process.argv[2]); // Get movie ID from the second argument

if (!movieId) {
  console.error('Please provide a Star Wars movie ID as an argument.');
  process.exit(1);
}

printMovieCharacters(movieId);
