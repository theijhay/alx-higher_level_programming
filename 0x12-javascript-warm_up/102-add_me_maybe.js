#!/usr/bin/node
// unction that increments and calls a function.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
