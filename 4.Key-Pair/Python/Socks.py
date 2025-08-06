def Paired_Stocks(stocks,N):
  
  stocks_count = {}
  pairs = 0
  for stock in stocks:
    if stock in stocks_count:
      stocks_count[stock] += 1
    else:
      stocks_count[stock] = 1
  
    if stocks_count[stock] % 2 ==0:
      pairs += 1
  return pairs 


N = int(input())
arr = list(map(int,input().split()))

res = Paired_Stocks(arr,N)
print(res)