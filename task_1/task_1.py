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


def sliding_window(measurements):
	count = sum([sum([m1, m2, m3]) < sum([m2, m3, m4]) for m1, m2, m3, m4 in zip(measurements, measurements[1:], measurements[2:], measurements[3:])])
	return count


if __name__ == '__main__':
	arr = read_file("measurements.txt")
	res = count_increase(arr)
	res_window = sliding_window(arr)
	print(str(res) + " measurements are larger than the previous one.")
	print(str(res_window) + " measurements are larger than the previous one in the sliding window approach.")
