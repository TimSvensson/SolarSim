import Universe
import Draw
import pygame
import sys
import os

class Main:

	def __init__(self, filename, width, height):

		self.draw 			= Draw.Window(width, height)
		self.clock 			= pygame.time.Clock()

		self.done 			= False
		self.moveDir 		= [False, False, False, False] # up, right, down, left

		self.kCycle 		= 0.0
		self.scale 			= 12
		self.position 		= Universe.Bodies.Point(0, 0)
		self.secPerCycel 	= -2

		self.uni 			= self.get_universe( filename )

		self.uni.printUni()



	def main_loop(self):

		cycle = 0

		while not self.done:

			self.clock.tick(100)

			self.get_input()

			self.uni.updateUniverse( )
			self.draw.updateDisplay( self.uni.bodies, self.kCycle, self.scale, self.position.x, self.position.y )

			if cycle == 100:
				self.kCycle += 0.1
				cycle = 0

			cycle += 1



	def get_input(self):
		for event in pygame.event.get():	# User did something
			self.handle_input(event)

		for i in xrange(0, 4): 				# moves the "camera".
			if self.moveDir[i] == True:
				self.changePositioin(i)

	def changePositioin(self, direction):
		if direction == 0: 		# move up
			self.position.y += 10**(self.scale)
		elif direction == 1: 	# move right
			self.position.x += 10**(self.scale)
		elif direction == 2: 	# move down
			self.position.y -= 10**(self.scale)
		elif direction == 3: 	# move left
			self.position.x -= 10**(self.scale)

	def handle_input(self, event):

		if event.type == pygame.QUIT:	# If user clicked close
				pygame.quit() 				# Exit the game and close everything
				sys.exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_KP_PLUS:
				self.secPerCycel += 1
			elif event.key == pygame.K_KP_MINUS:
				self.secPerCycel -= 1

			elif event.key == pygame.K_UP:
				self.moveDir[0] = True
			elif event.key == pygame.K_RIGHT:
				self.moveDir[1] = True
			elif event.key == pygame.K_DOWN:
				self.moveDir[2] = True
			elif event.key == pygame.K_LEFT:
				self.moveDir[3] = True

		elif event.type == pygame.KEYUP:

			if event.key == pygame.K_UP:
				self.moveDir[0] = False
			elif event.key == pygame.K_RIGHT:
				self.moveDir[1] = False
			elif event.key == pygame.K_DOWN:
				self.moveDir[2] = False
			elif event.key == pygame.K_LEFT:
				self.moveDir[3] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:

			if pygame.mouse.get_focused():
				
				if event.button == 4:
					self.scale -= 1
				elif event.button == 5:
					self.scale += 1

	def get_universe(self, filename):

		w_bodies = self.get_system(filename)

		uni = []

		for body in w_bodies:
			uni.append(Universe.Bodies.Body( body[0],body[1],body[2],body[3],body[4],body[5],body[6], ))

		return Universe.Universe( uni )

	def get_system(self, filename):

		word_list = self.load_file(filename)

		print word_list

		uni = []
		tmp_lst = []

		for word in word_list:
			
			try:
				tmp_lst.append(float(word))
			except ValueError:
				tmp_lst.append(word)

			if len(tmp_lst) == 7:
				uni.append(tmp_lst)

				print tmp_lst

				tmp_lst = []
				
		return uni

	def load_file(self,filename):

		file_location = os.path.join(os.path.dirname(__file__), filename)

		with open(file_location, 'r') as f:
			lines = f.read().split()

		return lines



width = 800
height = 600

system_filename = 'system.txt' # Relative path to the "solar system".



main = Main( system_filename, width, height )

main.main_loop()



pygame.quit()
sys.exit()