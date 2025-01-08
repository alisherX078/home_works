def func(nums, num, position=0):
    nums.insert(position, num)

func([1, 2, 3, 4, 5], 10, 4)
func([1, 2, 3, 4, 5], 10)