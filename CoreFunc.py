def unwrap(input):

	input = "|".join(input)
	input = input.replace("(", "")
	input = input.replace(")", "")
	input = input.split("|")

	return input

if __name__ == "__main__":
	print("Intended use as module")