#create a function that returns user's "digit of life"
#designed to enter date in YYYY-DD-MM format
def digit_of_life(date):
	date = date.split("-")
	dig_sum = 0
	for block in date:
		for num in block:
			dig_sum += int(num)
	if len(str(dig_sum)) >= 2:
		sum_ = 0
		count = 0
		while len(str(dig_sum)) >= 2:
			if count == 0:
				sum_str = str(dig_sum)
				for char in sum_str:
					sum_ += int(char)
					dig_sum = sum_
					count += 1
			else:
				sum_str = str(sum_)
				for char in sum_str:
					sum_ += int(char)
					dig_sum = sum_
	return dig_sum

print(digit_of_life("1996-16-10"))
