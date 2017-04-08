import Bodies

class Universe:

	def __init__(self, bodies):
		self.bodies = bodies

	def updateUniverse(self):
		for body in self.bodies:
			body.changeVelocity(self.bodies)
			body.changePosition()

	def printUni(self):
		for body in self.bodies:
			body.printBody()

	def addBody(self, body):
		self.bodies.append(body)