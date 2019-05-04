import React from 'react';
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
    if (this.state.tags.length === 0) {
        return ""
    }

    const inMax = this.state.tags[0].count
    const inMin = this.state.tags[this.state.tags.length - 1].count
    const outMin = 10
    const outMax = 100
    const tags = this.state.tags.map((tag) => {
        const count = tag.count
        const value = Math.ceil(
            ((count - inMin) / (inMax - inMin)) * (outMax - outMin) + outMin
        )
        return {text: tag.term, value: value}
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
