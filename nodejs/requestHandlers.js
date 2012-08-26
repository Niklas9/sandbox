function start(res)
{
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('hello Start');
}

function asdf(res)
{
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('hello ASDF');
}

exports.start = start;
exports.asdf = asdf;
