#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the SWAPI /films/ endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

// Send a GET request to the SWAPI
request(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  // Parse the response body as JSON
  const film = JSON.parse(body);

  // Get the list of character URLs
  const characterUrls = film.characters;

  // Fetch each character
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('An error occurred:', error);
        return;
      }

      // Parse the response body as JSON
      const character = JSON.parse(body);

      // Print the character's name
      console.log(character.name);
    });
  });
});
