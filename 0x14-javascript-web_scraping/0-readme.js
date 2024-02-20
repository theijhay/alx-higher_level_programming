#!/usr/bin/node

const filePath = process.argv[2];
const fs = require('fs');
fs.readFile(filePath, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
