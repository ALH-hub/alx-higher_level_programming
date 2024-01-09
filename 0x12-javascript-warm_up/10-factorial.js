#!/usr/bin/node

const num = Number(process.argv[2]);

function recursiveFactorial (a) {
  if (a <= 1) return 1;
  const fact = a * recursiveFactorial(a - 1);
  return (fact);
}

let fact;
if (!num) fact = 1;
else fact = recursiveFactorial(num);

console.log(fact);
