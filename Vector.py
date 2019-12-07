from manimlib.imports import *

class Vector(Scene, Vector):
	"""Clase Vector: admite suma, producto punto, etc."""
	CONFIG = {
        "camera_config": {"frame_center": 2*UP+2*RIGHT}
	}
	self.origen = (0,0,0)
	def __init__(self, v, coord):
		"""v: nombre, coord: coordenadas c/r al origen """
		self.nombre = "\\vec{"+v+"}"
		self.coord = coord

	def setOrigen(self, origen):
		self.origen = origen

	def getCoord(self):
		return self.coord

	def getNombre(self):
		return self.nombre
		

