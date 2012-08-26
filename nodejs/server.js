var http = require('http');
var url = require('url');

var port = 1337;

function start(route, handle) 
{
    http.createServer(function (req, res)
    {
        var path = url.parse(req.url).pathname;
        console.log('Request received '+ path +'.');
        route(handle, path, res);
    }).listen(port);

   console.log('server running at :'+ port +'\n'); 
}

exports.start = start;
