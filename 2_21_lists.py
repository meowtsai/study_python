# list is ordered
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

print(months[0])
print(months[1])
print(months[7])
print(months[-1])

#list slicing , first is inclusive, second is not
q3 = months[6:9]
print(q3)

#list slicing , omit first shows inclusive from the begining
first_half = months[:6]
print(first_half)

# in of not in: membership operator
print('Sunday' in months) # False
print('Feb' in months) # True

print('Saturday' not in months) # True

# Mutability