#!/usr/bin/node
/**
 * This script prits the first argument passed to it
 */
if (process.argv[3] === null) {
  console.log('No argument');
} else {
  console.log(process.argv[3]);
}
