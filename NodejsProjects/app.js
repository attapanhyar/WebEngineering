const os = require('os');

var totalMemory = os.totalmem()/(8*1024*1024*1024);
var freemem = os.freemem()/(8*1024*1024*1024);

console.log('Total Memory'+totalMemory);
console.log('Free Memory'+freemem);