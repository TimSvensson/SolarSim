import math

class Body:
	"""
	Represents a pysical body in the Univers.
	"""

	def __init__(self, name, x, y, dx, dy, mass, radius):
		self.name		= name 			# The name of the celestial body.
		self.center		= Point(x, y)	# The center of the body in reference to the "univers".
		self.deltaPoint	= Point(dx, dy) # The change in position in reference to the center of the body.
		self.mass 		= mass 			# The mass of the body.
		self.radius 	= radius 		# The radius of the body measured in pixels. 1 pixel = 1*10**9 m



	def changeVelocity(self, otherBodies):
		"""
		Updates the body's velocity by calculating the force pull of all the different bodies in the universe using "Newton's theory of gravitation" and adding the resulting velocity to the body's current velocity.
		"""

		for body in otherBodies:
			if self != body:
				self.newVelocity(body)

	def newVelocity(self, otherBody):
		"""
		Calculates the new velocity of this body using "Newton's theory of gravitation".
		"""

		d = math.hypot(( self.center.x - otherBody.center.x ), ( self.center.y - otherBody.center.y ))
		a = math.atan2(( otherBody.center.y - self.center.y ), ( otherBody.center.x - self.center.x ))
		f = self.getF(self.mass, otherBody.mass, d )

		self.deltaPoint.x += math.cos(a) * f / self.mass
		self.deltaPoint.y += math.sin(a) * f / self.mass

	def getF(self, m1, m2, d):

		# The gravitational constant.
		g = 6.6738480 * 10**(-11)

		return g * m1 * m2 / d**2

	def changePosition(self):
		"""
		Applies the change in position to the current position.
		"""

		self.center.x += self.deltaPoint.x
		self.center.y += self.deltaPoint.y

	def printBody(self):
		"""
		Prints the information of the body.
		"""

		print 'Name: {}'.format(self.name)
		print 'Position: ({}, {})'.format(self.center.x, self.center.y)
		print 'Velocity: ({}, {})'.format(self.deltaPoint.x, self.deltaPoint.y)
		print 'Mass: {}'.format(self.mass)
		print 'Radius: {}\n'.format(self.radius)

		

class Point:
	"""
	Defines a center on a 2d plane using a x and a y coordinate.

	Also used to store the change in position over time since velocity can be seen as the change in the x- and the y-coordinate over time.
	"""

	def __init__(self, x, y):
		self.x = x
		self.y = y