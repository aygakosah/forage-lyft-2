from tire.tire import Tire


class OctoPrimeTire(Tire):
	def __init__(self, tire_values):
		self.tire_values = tire_values

	def needs_service(self):
		total = 0.0
		for val in self.tire_values:
			total = total + val
		if total >= 3.0:
			return True
		return False
