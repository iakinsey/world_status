import React from 'react';
import Map from "./views/map"
import ArticleFeed from "./views/feed"
import {listen} from "./listener";
import {getPolarizingValue, getPolarityColor} from "./util";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {}
    this.listeners = {
        article: [],
        tag_cloud: []
    }

    listen({}, (msg) => this.handleMessage(msg))
  }

  handleMessage(msg) {
    const data = JSON.parse(msg.data)
    const listeners = this.listeners[data.message_type]

    if (!listeners) {
        return
    }

    for (var i = 0; i < listeners.length; i += 1) {
        var listener = listeners[i]
        listener(data.data)
    }
  }

  render() {
    return (
      <span>
        <Map listeners={this.listeners} />
        <ArticleFeed listeners={this.listeners} />
      </span>
    )
  }
}

export default App;
