var http = require('http');
var url = require('url');

var port = 1337;

http.createServer(function (req, res) {
    var path = url.parse(req.url).pathname;
    console.log('Request received '+ path +'.');
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('hello Niklas');
    res.end('\n');
}).listen(port);

console.log('Server running at :'+ port +'\n');
