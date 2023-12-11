#!/usr/bin/node
/**
 * This script prits the first argument passed to it
 */
const allArguments = process.argv;
if (allArguments.length <= 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < allArguments.length; i++) {
    console.log(process.argv[i]);
  }
}
