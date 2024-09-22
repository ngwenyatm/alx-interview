#!/usr/bin/node

const fetch = require('node-fetch'); // Assuming you're using Node.js

async function getStarWarsCharacters(filmId) {
  try {
    const filmResponse = await fetch(`https://swapi.dev/api/films/${filmId}`);
    const filmData = await filmResponse.json();

    const characterUrls = filmData.characters;

    for (const characterUrl of characterUrls) {
      const characterResponse = await fetch(characterUrl);
      const characterData = await characterResponse.json();
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <film_id>');
  process.exit(1);
}

const filmId = parseInt(process.argv[2]);
getStarWarsCharacters(filmId);