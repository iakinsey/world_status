import React from 'react';
import {getPolarizingValue, getPolarityColor} from "../util";

class ArticleFeed extends React.Component {
  constructor(props) {
    super(props)

    props.listeners.article.push((i) => this.updateArticles(i))
    this.state = {
      articles: []
    }
  }

  updateArticles(articles) {
    this.state.articles.unshift(articles)
    var newArticles = this.state.articles.slice(0, 50)
    this.setState({articles: newArticles})
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
        {articleList}
      </span>
    )
  }
}

export default ArticleFeed;
