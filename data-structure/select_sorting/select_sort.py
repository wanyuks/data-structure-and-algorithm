# coding: utf8

def select_sorting(l:list):
	n = len(l)
	for i in range(n-1):
		min_index = i
		for j in range(i+1, n):
			if l[j] < l[min_index]:
				l[j], l[min_index] = l[min_index], l[j]
	return l


if __name__ == "__main__":
	l = [4,7,2,8,3,9,1,87,32]
	print(select_sorting(l))
