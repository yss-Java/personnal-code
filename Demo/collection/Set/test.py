nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
nums2 = list(set(nums))
nums2.sort(reverse=True)
print(nums2)
print(sorted(list(set(nums)), reverse=True))
