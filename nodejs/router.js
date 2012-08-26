function route(handle, path, res)
{
    console.log('About to route request for '+ path);
    if( typeof handle[path] === 'function')
    {
        console.log('Calling request handler for '+ path);
        handle[path](res);
    }
    else
    {
        console.log('No request handler for '+ path);
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('Not found biatch!');
    }
}

exports.route = route;
