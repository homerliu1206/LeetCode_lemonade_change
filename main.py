class Solution:
    def lemonadeChange(self, bills):

        deposit = [] # record the money in present
        i = 0 # count the times of calculation

        for money in bills:
            if money == 5:
                deposit.append("5")
                i += 1
                # print(deposit)

            elif money == 10:
                if "5" in deposit:
                    deposit.append("10")
                    deposit.remove("5")
                    i += 1
                else:
                    print(False)
                    # return False
                    break
                # print(deposit)

            elif money == 20:
                if "10" in deposit or "5" in deposit:
                    if deposit.count("10") >= 1 and deposit.count("5") >=1:
                        deposit.append("20")
                        deposit.remove("5")
                        deposit.remove("10")
                        i += 1
                    elif deposit.count("5") >= 3:
                        deposit.append("20")
                        deposit.remove("5")
                        deposit.remove("5")
                        deposit.remove("5")
                        i += 1
                    else:
                        print(False)
                        # return False
                        break
                else:
                    print(False)
                    # return False
                    break
                # print(deposit)

        if i == len(bills):
            print(True)
            # return True

solution = Solution()
solution.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5])


# Input: bills = [5,5,5,10,20]
# Output: true

# Input: bills = [5,5,10,10,20]
# Output: false