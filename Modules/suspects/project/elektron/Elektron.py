'''Info Header Start
Name : Elektron
Info Header End'''

class Elektron:
	"""
	Elektron description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		print("Elektron init done", ownerComp)

	def OnMidi(self, rowIndex, message, index, value, input):
		'''
		MIDI Events
		'''
		if message == "Timing Clock":
			pass
		else:
			#print(rowIndex, message, index, value, input)
			if message == 'Start':
				op('constant4').par.value0 = 0
				op('constantStatus').par.value0 = 1
			if message == 'Stop':
				op('constant4').par.value0 = 0
				op('constantStatus').par.value0 = 0        

			if rowIndex == 101:
				if message == "Timing Clock":
					pass
			if message == 'Program Change':
				op('constantPattern').par.value0 = index - 1
	
	def Ping(self):
		# print("png")
		pass