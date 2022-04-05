def read_file(inpath):
	with open(inpath, 'r') as f:
		# read file and convert to integers
		nums = [int(x.strip()) for x in f.readlines()]
	f.close()
	return nums


def count_increase(measurements):
	# filter elements, then count 'True'
	count = sum([m1 < m2 for m1, m2 in zip(measurements, measurements[1:])])
	return count


if __name__ == '__main__':
	arr = read_file("measurements.txt")
	res = count_increase(arr)
	print(str(res) + " measurements are larger than the previous one.")
