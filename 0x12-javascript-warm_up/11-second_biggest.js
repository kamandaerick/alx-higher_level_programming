#!/usr/bin/node
/**
 * Find the second largest number in a list of args
 */
const a = process.argv;
const args = [];
for (let i = 2; i < a.length; i++) {
  args.push(a[i]);
}
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(args.sort().reverse()[1]);
}
