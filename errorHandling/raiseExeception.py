def squarefunc(num):
  try:
   return int(num)*int(num)
  except:
      raise ValueError("Please send a number")

print(squarefunc(5))
print(squarefunc('hello'))
