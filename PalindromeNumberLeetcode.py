class Solution:
    def isPalindrome(self, x: int) -> bool:
        #121 % 10 = 1 to get the ones place; left value
        # 121/100=1 to get hundreds place, this will tell how many hundreds there are; right value
        #121/10 = 12
        #121 % 100 = 21
        #21/10 = 2
        #ANY negative number is false

        if x < 0: return False

        div =1
        while x >=10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right: return False

            x = (x % div) // 10
            div = div / 100
        return True