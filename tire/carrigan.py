from tire.tire import Tire


class CarriganTire(Tire):
	def __init__(self, tire_values):
		self.tire_values = tire_values

	def needs_service(self):
		for val in self.tire_values:
			if val >= 0.9:
				return True
		return False

