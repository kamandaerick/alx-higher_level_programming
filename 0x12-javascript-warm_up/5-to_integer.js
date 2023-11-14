#!/usr/bin/node
/**
 * This script checks if the first cmdline argument 
 * can be converted to an integer and converts it
 */
const input = process.argv[2];

const convertedNumber = Number(input);

if (!isNaN(convertedNumber) && Number.isInteger(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log("Not a number");
}
