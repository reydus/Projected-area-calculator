var start = new Date()
var parse3DS = require('parse-3ds');
var fs = require('fs');
file = process.argv[2]
var buf = fs.readFileSync(file);
var parsed = parse3DS(buf, { 'objects':true, 'tree':false });
var parsed = parsed["objects"];
console.log(parsed)
console.log(typeof(parsed))
JSONer = JSON.stringify(parsed)
fs.writeFileSync("./everything.json",JSONer);
console.log("Stopping timer")
var timer = new Date() - start
var timer = timer / 1000
console.log("That took me "+timer+" seconds")
fs.writeFileSync("report.txt", timer)
console.log(process.cwd())