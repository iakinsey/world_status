module.exports.listen = function (filter, callback) {
    const url = "ws://127.0.0.1:5321" + "/" + getFilter(filter);
    const ws = new WebSocket(url);
    ws.onmessage = (event) => {
        callback(event);
    }
}

function getFilter(filter) {
    return btoa(JSON.stringify(filter))
}
