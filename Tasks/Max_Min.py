nums_array = [4,2,9,1,7,5]
maximum_num = nums_array[0]
minimum_num = nums_array[0]

for num in nums_array:
    if num > maximum_num:
        maximum_num = num
    if num < minimum_num:
        minimum_num = num

print(" Maximum Number is : ", maximum_num)
print(" Minimum Number is : ", minimum_num)
