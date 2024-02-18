#!/usr/bin/node
// Import the axios module
const axios = require('axios');

// Define an asynchronous function to get character names
async function getCharacterNames (movieId) {
  try {
    // Send a GET request to the SWAPI films endpoint with the movie ID
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);

    // Extract the list of character URLs from the response
    const characterUrls = response.data.characters;

    // Loop over each character URL
    for (const url of characterUrls) {
      // Send a GET request to each character URL
      const characterResponse = await axios.get(url);

      // Print the name of the character
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    // If there's an error, print it
    console.error(error);
  }
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Call the function with the movie ID
getCharacterNames(movieId);
