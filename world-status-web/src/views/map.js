/*global Datamap*/
import React from 'react';
import {getPolarity, getPolarityColor} from '../util'


class Map extends React.Component {
  constructor(props) {
    super(props)
    this.queue = []
    this.totals = {}
    this.counts = {}
    props.listeners.worldMap = (i) => this.addMapItem(i)
  }
 
  addMapItem(item) {
      if (!this.map) {
          this.queue.push(item)
          return
      }

      if (this.queue.length > 0) {
          for (var i = 0; i < this.queue.length; i++) {
              this.addColorToMap(this.queue[i]);
          }

          this.queue = []
      }

    this.addColorToMap(item)
  }

  addColorToMap(article) {
    const countries = article.countries

    if (!countries || countries.size === 0) {
        return
    }

    const polarity = getPolarity(article)

    for (var i = 0; i < countries.length; i++) {
        var country = countries[i]
        if (!this.totals[country]) {
            this.totals[country] = 0
            this.counts[country] = 0
        }

        this.totals[country] += polarity
        this.counts[country] += 1

        var average = this.totals[country] / this.counts[country]
        var color = getPolarityColor(average)
        var updateDict = {}
        updateDict[country] = color
        console.log(average)
        console.log(color)
        console.log(updateDict)
        this.map.updateChoropleth(updateDict)
    }
  }

  componentDidMount() {
      this.map = new Datamap({
          element: document.getElementById('map-widget'),
          fills: {
              defaultFill: "#cdcdcd"
          },
          geographyConfig: {
              borderColor: "#333",
              highlightFillColor: '#6f6f6f',
              highlightBorderColor: "#333",
              highlightBorderWidth: 1
          }
      });
  }
    
  render() {
    return (
        <div style={mapWidgetStyle} id="map-widget">
        </div>
    );
  }
}

const mapWidgetStyle = {
    height: '600px',
    width: "1600px",
    margin: "auto"
}

export default Map;
