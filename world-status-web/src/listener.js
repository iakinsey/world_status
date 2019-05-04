module.exports.listen = function (filter, callback) {
    initiateWebsocket(filter, callback)
}


function initiateWebsocket(filter, callback) {
    var url = "ws://127.0.0.1:5321/" + getFilter(filter);
    const ws = new WebSocket(url);

    ws.onmessage = (event) => {
        callback(event);
    }

    ws.onclose = (event) => {
        filter.send_initial_messages = false
        initiateWebsocket(filter, callback)
    }

    setTimeout(function(){
        ws.close()
    }, 3000);
}

function getFilter(filter) {
    return btoa(JSON.stringify(filter))
}
