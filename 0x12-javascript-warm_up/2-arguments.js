#!/usr/bin/node
/**
 * This script checks for the number of commandline arguments
 * and prints the appropriate message
 */

const allArguments = process.argv;

if (allArguments.length === 2) {
  console.log('No argument');
} else if (allArguments.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

