# coding: utf8

# 升序排序
def bubble_sorting(sort_list):
	n = len(sort_list)
	for i in range(n-1):
		for j in range(n-1-i):
			if sort_list[j] > sort_list[j+1]:
				sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
	return sort_list


if __name__ == "__main__":
	l = [1,5,3,9,7,6,2]
	print(bubble_sorting(l))