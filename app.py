import ee
from ee_plugin import Map


img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
region = ee.Geometry.BBox(-122.0859, 37.0436, -122.0626, 37.0586)

image = ee.Image('USGS/SRTMGL1_003').unitScale(0, 5000)

Map.addLayer(image, {'palette': ['blue', 'red'], 'min': 0, 'max': 1000}, 'dem', True)
