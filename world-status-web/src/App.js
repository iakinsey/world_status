import React from 'react';
import Map from "./views/map"
import {listen} from "./listener";
import {getPolarizingValue, getPolarityColor} from "./util";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      articles: []
    }
    this.listeners = {}
    listen({}, (msg) => this.handleMessage(msg))
  }

  handleMessage(msg) {
    const data = JSON.parse(msg.data)

    if (data.message_type === "article") {
        this.state.articles.unshift(data.data)

        var newArticles = this.state.articles.slice(0, 50)

        this.setState({"articles": newArticles})

        if (this.listeners.worldMap) {
            this.listeners.worldMap(data.data);
        }
    }
  }

  render() {
    const articleList = this.state.articles.map((article) => {
      const polarity = getPolarizingValue(article, "polarity")
      const color = getPolarityColor(polarity)

      return (
        <div key={article.url}> 
          <a 
           href={article.url}
           style={{
             color: color,
             textDecoration: 'none'
           }}>
           {article.title_text}
          </a>
        </div>
      )
     })

    return (
      <span>
        <Map listeners={this.listeners} />
        {articleList}
      </span>
    )
  }
}

export default App;
