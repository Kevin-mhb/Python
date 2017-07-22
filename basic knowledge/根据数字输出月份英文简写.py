#当输入一个月份的数字代号时，相应的输出它的英文缩写

print("Please input a number of a month:\n")
months="JanFebMarAprMayJunJulAugSepOctNovDec"
i=int(input())
begin=3*i-3

print("This month is "+months[begin:(begin+3)]+" .\n")
