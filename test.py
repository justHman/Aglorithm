def totalNumbers(digits) -> int:
        evens = []
        def permutate(digits, nums = []):
            nonlocal evens
            if len(nums) == 3:
                number = int(''.join(nums))
                if number % 2 == 0 and len(str(number)) == 3 and number not in evens:
                    evens.append(number)
                return 
            
            for digit in digits:
                nums.append(str(digit))
                flt_digits = []
                c = 0
                for v in digits:
                    if v == digit and c != 1:
                        c = 1
                        continue
                    flt_digits.append(v)
                permutate(flt_digits, nums)
                nums.pop()
        permutate(digits)
        return len(evens)

rs = totalNumbers([1, 3, 5])
print()
print(rs)