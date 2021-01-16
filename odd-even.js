// Submitted by: Rommy Gustiawan

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Input numbers : ', (numbers) => {
  const odd = [];
  const even = [];

  numbers.split(',').forEach((value) => {
    value % 2 != 0 ? odd.push(value) : even.push(value);
  });

  console.log(`Odd Numbers   : ${odd}`);
  console.log(`Even Numbers  : ${even}`);

  readline.close();
});
