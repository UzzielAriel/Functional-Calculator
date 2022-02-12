import CoreFunc

operators = ["+", "-", "*", "/"]

class Calc:
	def __init__(self, input):
		
		self.mi = False
		self.count = 0
		self.ic = 0
		self.operator = []
		self.input = input
		self.n = 0
		self.curr_val = 0
		self.b = 0
		self.input = self.input.replace(" ", "")

		self.input = CoreFunc.multb(self.input)

		for i in range(len(self.input)):
			if self.input[i] in operators:
				if i > 0:
					if self.input[i-1] == "(":
						continue
				self.operator.append(self.input[i])
				self.count += 1
		

		if self.count > 1:
			self.mi = True
			
			self.input = list(self.input)

			for x in range(len(self.input)):
				for i in self.operator:
					if self.input[x-1] == "(" and i == self.input[x]:
							self.input[x] = i
					elif i == self.input[x]:
						self.input[x] = " "

			self.input = "".join(self.input)

			self.input = self.input.split(" ")
			self.input = CoreFunc.unwrap(self.input)
			for i in range(len(self.input)):
				self.input[i] = int(self.input[i])


			for i in range(len(self.input)):
				if i + 2 > len(self.input):
					break
				if i == 0:
					self.a = self.input[i]
				self.b = self.input[i+1]
				self.getop()
				self.a = self.curr_val
				self.n += 1
				
			print(self.curr_val)
					

		if self.mi == False:

			self.input = list(self.input)

			for x in range(len(self.input)):
				for i in self.operator:
					if self.input[x-1] == "(" and i == self.input[x]:
							self.input[x] = i
					elif i == self.input[x]:
						self.input[x] = " "

			self.input = "".join(self.input)
			self.input = self.input.split(" ")
			self.input = CoreFunc.unwrap(self.input)
			self.a = int(self.input[0].strip())
			self.b = int(self.input[1].strip())

			self.getop()
			print(self.curr_val)

	def getop(self):
		match self.operator[self.n]:
			case"+":
				self.add()
			case "-":
				self.sub()
			case "*":
				self.mult()
			case "/":
				self.divide()

	def add(self):
		self.curr_val = self.a + self.b

	def sub(self):
		self.curr_val = self.a - self.b
	
	def mult(self):
		self.curr_val = self.a * self.b
	
	def divide(self):
		self.curr_val = self.a / self.b

Calc(input())