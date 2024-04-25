#!/usr/bin/node

exports.logMe = function (item) {
  let count = 0;
  if (item) {
    console.log(count + ' : ' + item );
    count++;
  }
};
