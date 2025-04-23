def longest_palindrome(s):
    if not s:
        return ""

    def expand_around_center(left, right):
        while left > 0 and right < len(s) and s[left] == s[right]:
            print(s[left], s[right])
            left -= 1
            right += 1
        # Trả về chuỗi đối xứng tìm được (bỏ đi ký tự thừa cuối cùng)
        print(s[left:right])
        return s[left:right]

    longest = ""
    for i in range(len(s)):
        # Trường hợp tâm là 1 ký tự
        odd_pal = expand_around_center(i, i)
        # Trường hợp tâm là 2 ký tự
        even_pal = expand_around_center(i, i + 1)

        # Lấy chuỗi đối xứng dài hơn
        longest = max(longest, odd_pal, even_pal, key=len)

    return longest



if __name__ == "__main__":
    s = "cbbd"
    print(longest_palindrome(s))