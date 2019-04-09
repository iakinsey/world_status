export function getPolarity(article) {
  const polarities = [
      article.content_polarity,
      article.summary_polarity,
      article.title_polarity
  ].filter((n) => !isNaN(n))
  const max = Math.max(...polarities)
  const min = Math.min(...polarities)
  const maxDistance = 1 - max
  const minDistance = 1 + min
   
  if (maxDistance > minDistance) {
      return min
  } else if (maxDistance < minDistance) {
      return max
  } else if (maxDistance === minDistance && maxDistance !== 0) {
    return polarities.reduce((t, n) => t + n) / polarities.length
  }

  return 0
}

export function getPolarityColor(polarity) {
  if (1 >= polarity && polarity > 0.5) {
    return "#00ff00"
  } else if (0.5 >= polarity && polarity > 0) {
    return "#cbffc9"
  } else if (0 > polarity && polarity > -0.5) {
    return "#ffc9c9"
  } else if (-0.5 >= polarity && polarity > -1) {
    return "#ff1515"
  }
  return "#cdcdcd"
}
