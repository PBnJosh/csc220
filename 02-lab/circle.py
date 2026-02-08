import point
import color

class Circle :
  def __init__( self, center, radius, fill ):
    self._center = center
    self._fill = fill
    self._radius = radius

  def setCenter( self, new_center ):
    self._center = new_center

  def setFill( self, new_fill):
    self._fill = new_fill

  def setRadius( self, new_radius ):
    self._radius = new_radius

  def getCenter( self ):
    return self._center
  
  def getFill( self ):
    return self._fill

  def getRadius( self ):
    return self._radius

  def SVG( self ):
    return f"<circle r={self._radius} cx={self.center.getAcross()} cy={self.center.getDown()} fill={self.fill.SVG()} />"