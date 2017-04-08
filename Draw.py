import math
import pygame
pygame.init()

cBlack = ( 25, 25, 25 )
cWhite = ( 200, 200, 200 )
cGrey  = ( 100, 100, 100 )

class Window:

	def __init__(self, width, height):
		self.screenSize = [width, height]
		self.display 	= pygame.display.set_mode(self.screenSize)
		self.font 		= pygame.font.SysFont(None, 12)
		self.screenX 	= 0
		self.screenY 	= 0
		self.scale 		= 12

		pygame.display.set_caption( 'Solar Sim' )



	def updateDisplay(self, objects, crntCycle, crntScale, x, y):
		self.display.fill(cBlack)

		self.screenX = x
		self.screenY = y
		self.scale = crntScale



#		pygame.draw.line(self.display, cGrey, [0, self.screenSize[1] / 2], [self.screenSize[0], self.screenSize[1] / 2], 1)
#		pygame.draw.line(self.display, cGrey, [self.screenSize[0] / 2, 0], [self.screenSize[0] / 2, self.screenSize[1]], 1)
#
		pygame.draw.circle(self.display, cGrey, [self.screenSize[0] / 2, self.screenSize[1] / 2], 15, 1)
#		pygame.draw.circle(self.display, cGrey, [self.screenSize[0] / 2, self.screenSize[1] / 2], 108, 1)
#		pygame.draw.circle(self.display, cGrey, [self.screenSize[0] / 2, self.screenSize[1] / 2], 148, 1)
#		pygame.draw.circle(self.display, cGrey, [self.screenSize[0] / 2, self.screenSize[1] / 2], 217, 1)

		

		for obj in objects: # Draw all celestial bodies
			x = self.getX(obj)
			y = self.getY(obj)
			r = self.getRadius(obj)

			if math.fabs(x) <= self.screenSize[0] + r and math.fabs(y) <= self.screenSize[1] + r:
				pygame.draw.circle(self.display, cWhite, [x, y], r, 0)
				self.drawObjectName( obj.name, r, x, y )

		self.drawCrntCycle( crntCycle )
		self.drawCrntPositionAndScale()

		pygame.display.flip()



	def drawCrntCycle(self, crntCycle):
		label = self.font.render( 'kCycles: {:0.1f}'.format( crntCycle ), 1, cGrey )
		self.display.blit( label, ( 10, 10 ))

	def drawObjectName(self, name, radius, x, y):
		label = self.font.render( '{}'.format(name), 1, cGrey )
		self.display.blit( label, ( x + radius + 5, y + 5 ))

	def drawCrntPositionAndScale(self):
		label = self.font.render( 'Position: ( x {:.1f}, y {:.1f} )     Scale: 1.0 e {:.1f} m / pixel'.format( self.screenX, self.screenY, self.scale ), 1, cGrey )
		self.display.blit( label, ( 20, self.screenSize[1] - 20 ))

	def getX(self, obj):

		return int( self.screenSize[0] / 2 + (( obj.center.x - self.screenX ) / math.pow( 10, self.scale ) ))

	def getY(self, obj):

		return int( self.screenSize[1] / 2 - (( obj.center.y - self.screenY ) / math.pow( 10, self.scale ) ))

	def getRadius(self, obj):

		r = obj.radius / math.pow( 10, self.scale )

		if r < 1:
			r = 1

		return int(r)

