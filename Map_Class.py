

map_height = 8
map_width = 50

class map():
	def __init__(self):
		self.size = {'height':map_height,'width':map_width}
		self.grid = []
		self.wallMarker = 'X'
		self.reset()
		self.makeWalls()

	def reset(self):
		self.grid = []
		for i in range(self.size['height']):
			self.grid.append([])
			for ix in range(self.size['width']):
				self.grid[i].append(' ')


	def makeWalls(self):
		for i in range(len(self.grid)):
			self.grid[i][0] = self.wallMarker
			self.grid[i][-1] = self.wallMarker
		for ix in range(-1,1,1):
			for iy in range(0,self.size['width']):
				self.grid[ix][iy] = self.wallMarker


	def showMap(self):
		for i in range(self.size['height']):
			print(''.join(self.grid[i]))
