# gpxMap
Animate GPS data. Use and gpx file to display your GPS data.

```
import gpxMap

graph = gpxMap.Graphics("Teusaca.gpx")
graph.setMapType('satellite') # maptypes: roadmap, satellite, terrain, hybrid

jump = graph.getNumberPoints() // (10 * 24) # 10 seconds

graph.animate(jump = jump)
```

![Results](https://github.com/jsbarbosa/gpxMap/blob/master/Sopo.gif)

![Results](https://github.com/jsbarbosa/gpxMap/blob/master/Teusaca.gif)
