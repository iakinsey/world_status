import React from 'react';

class Feed extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        articles: props.articles
    }
  }
  
  render() {
    return (
        this.state.articles.map((article) => {
            return <div>N/A</div>
        })
    );
  }
}

export default Feed;
