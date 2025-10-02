count = 0
limit = 85200
squaredTotals = 0
squared = 0
while True:
    
    squared = count*count
    if(squared%2==1):
        squaredTotals+=squared

    count += 1
    if count > limit:
        break
print(squaredTotals)