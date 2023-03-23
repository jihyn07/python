isinNumber = int(input('ISIN 숫자를 입력해주세요: '))

list1 = []
n = 1

for i in range(isinNumber):
    i = input('ISIN을 입력해주세요: ')  
    list1.append(i) 
# print(list1[0])
    #  예 : KR103501GA68
    #       KR574401BAA2

for n in range(isinNumber):
    print(list1[n])