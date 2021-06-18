# class Solution:
#     def result(self):
#         return 1

# if __name__ == "__main__":
#     s = Solution()
#     print(s.result())

# def get_natural_number():
#     n = 0
#     while True:
#         n += 1
#         yield n

# g = get_natural_number()
# for _ in range(0,100):
#     print(next(g))
    

# print("test git!!!_210526")
# print("1")
# print("test_0529")


num = 987

# mod_num = list(map(int, str(num)))
print([int(i) for i in str(num)])
sum = 0

for i in mod_num:
    sum += i


print(sum)
