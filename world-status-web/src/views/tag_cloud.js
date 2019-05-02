import React from 'react';
import TagCloud from 'react-tagcloud'
import { render } from "react-dom";
import WordCloud from "react-d3-cloud";

class TagCloudView extends React.Component {
  constructor(props) {
    super(props)

    props.listeners.tag_cloud.push((i) => this.updateCloud(i))
    this.state = {
        tags: []
    }
  }

  updateCloud(tags) {
      this.setState({tags: tags})
  }

  render() {
    if (!this.state.tags) {
        return ""
    }

    const tags = this.state.tags.map((tag) => {
        return {text: tag.term, value: tag.count}
    })

    return (
        <WordCloud
         font={'"Lucida Console", Monaco, monospace'}
         width={parseInt(window.innerWidth*.4)}
         data={tags} />
    )
  }
}

export default TagCloudView
