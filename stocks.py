stocks=[215,265,250,200,240,260,230]
minSoFar=float('inf')
maxProfit=0
for i in stocks:
    minSoFar=min(minSoFar,i)
    maxProfit=max(maxProfit,i-minSoFar)
print(maxProfit)    
