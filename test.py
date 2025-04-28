
def my_permutation(nums):
    def back_track(nums, so = []):
        if len(so) == 3:
            print(''.join(so))
            return 
        
        for num in nums:
            so.append(str(num))
            a = [v for v in nums if v != num]
            back_track(a, so)
            so.pop()
    back_track(nums)
            

nums = [1, 2, 3]
my_permutation(nums)

