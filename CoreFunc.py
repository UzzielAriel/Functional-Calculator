

def multb(input):
	input = list(input)
	for i in range(len(input)):
		if i > 0:
			if i + 1 < len(input):
				if input[i] == ")" and input[i+1] == "(":
					input[i] = input[i] + "*"
				elif input[i] == "(" and input[i-1].isdigit():
					input[i] = "*" + input[i]
				elif input[i] == ")" and input[i+1].isdigit():
					input[i] = input[i] + "*"
	input = "".join(input)
	return input

def unwrap(input):

	input = "|".join(input)
	input = input.replace("(", "")
	input = input.replace(")", "")
	input = input.split("|")

	return input

if __name__ == "__main__":
	print("Intended use as module")