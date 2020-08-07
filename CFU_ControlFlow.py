# CFU_ControlFlow.py
#The kindof loop used is a for loop
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
number = []
summ = []
for num in num_list:
    if num % 2 == 1:
        number.append(num)

if len(number) > 5:
    Num = sum(number[0:5])
    summ.append(Num)
    print(Num)