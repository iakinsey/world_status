import React from 'react';
import Map from "./views/map"
import ArticleFeed from "./views/feed"
import TagCloudView from "./views/tag_cloud"
import {listen} from "./listener";

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
        <div>
            <div style={{width: "50%", "float": "right"}}>
                <TagCloudView listeners={this.listeners} />
            </div>
            <div style={{width: "50%", "float": "left"}}>
                <ArticleFeed listeners={this.listeners} />
            </div>
        </div>
      </span>
    )
  }
}

export default App;
