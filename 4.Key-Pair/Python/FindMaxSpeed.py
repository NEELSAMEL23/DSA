def solve(n, arr):
  
  car_speed = {}
  
  for speed in arr:
    if speed in car_speed:
      car_speed[speed] += 1
    else:
      car_speed[speed] = 1
  
  max_speed = max(car_speed.keys())
  
  max_cars_count = car_speed[max_speed]
  
  print(max_cars_count)
  