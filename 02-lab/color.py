Class color :
  def __init__( self ):
    self._red = 0
    self._green = 0
    self._blue = 0
  
  def getRed( self ):
    return self._red

  def getGreen( self ):
    return self._green

  def getBlue ( self ):
    return self._blue
  
  def setRed( self, new_red ):
    self._red = new_red
  
  def setGreen( self, new_green ):
    self._green = new_green

  def setBlue( self, new_blue ):
    self._blue = new_blue

  def SVG( self ):
    return f"rgb({self._red}, {self._green}, {self._blue})"