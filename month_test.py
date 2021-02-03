months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))

month_begin = 3*(n-1)
month_end = 3*(n-1)+3

print(months[month_begin:month_end])
