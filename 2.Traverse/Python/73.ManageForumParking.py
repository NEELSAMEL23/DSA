
def is_parking_possible(k,arrival,departure):
  
  events = []
  
  for i in range(len(arrival)):
    events.append((arrival[i],1))
    events.append((departure[i],1))
  
  events.sort()
  
  current_cars = 0
  
  for _ , event in events:
    current_cars += event
    if current_cars > k:
      return "Not Possible"
  
  return "Possible"






k = int(input())

arrival = list(map(int,input().split()))
departure = list(map(int,input().split()))

print(is_parking_possible(k,arrival,departure))