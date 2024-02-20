#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'http://swapi.co/api/films/' + episode;

request(url, function (err, data, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
