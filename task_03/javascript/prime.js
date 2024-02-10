const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a positive number: ', (userInput) => {
for (i=2;i<userInput;i++){
isprime = true;
for (j=2;j<i;j++){
if(i%j==0){
isprime = false;
break;
}
}
if (isprime==true){
  console.log(i);
  }
}
  rl.close();
});


