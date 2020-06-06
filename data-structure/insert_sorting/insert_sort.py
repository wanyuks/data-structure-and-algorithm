# coding: utf8

def insert_sorting(l:list):
	n = len(l)
	for i in range(1, n):
		j = i
		while j > 0:
			if l[j] < l[j-1]:
				l[j], l[j-1] = l[j-1], l[j]
			else:
				break
			j -= 1
	return l


if __name__ == "__main__":
	l = [4,2,6,23,12,76,35]
	print(insert_sorting(l))
