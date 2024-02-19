#!/usr/bin/node
const axios = require('axios');
const process = require('process');

async function getMovieCharacters(movieId) {
    try {
        const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const movieData = response.data;
        const charactersUrls = movieData.characters || [];

        const characters = await Promise.all(
            charactersUrls.map(async (characterUrl) => {
                const characterResponse = await axios.get(characterUrl);
                return characterResponse.data.name;
            })
        );

        return characters;
    } catch (error) {
        console.error(`Failed to retrieve data for Movie ID ${movieId}.`);
        return [];
    }
}

async function main() {
    if (process.argv.length !== 3) {
        console.error("Usage: node script.js <Movie ID>");
        process.exit(1);
    }

    const movieId = process.argv[2];
    const characters = await getMovieCharacters(movieId);
    
    if (characters.length > 0) {
        characters.forEach(character => console.log(character));
    } else {
        console.log("No characters found for the provided Movie ID.");
    }
}

main();

