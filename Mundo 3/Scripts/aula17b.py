nums = [4, 2, 3, 7, 9]
nums[2] = 5
nums.append(12)
nums.insert(4, 0)
nums.pop(4)
if 4 in nums:
    nums.remove(4)
else:
    print('4 não está na lista! :(')
nums.sort(reverse=True)
print(nums)
print(f'Essa lista tem {len(nums)} elementos.')