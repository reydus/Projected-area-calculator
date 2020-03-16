var parse3DS = require('parse-3ds');
var fs = require('fs');
 
var buf = fs.readFileSync('T3A taper headframe fit.3ds');
var parsed = parse3DS(buf, { 'objects':true, 'tree':false });
var parsed = parsed["objects"];

console.log(parsed)
console.log(typeof(parsed))

JSONer = JSON.stringify(parsed)

fs.writeFileSync("./everything.json",JSONer);

