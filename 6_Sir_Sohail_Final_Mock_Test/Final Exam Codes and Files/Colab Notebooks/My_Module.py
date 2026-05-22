def calc(num1, num2, operator):
  """ num1 : int
      num2 : int
      operator : + - * /
  """
  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2
  else:
    result = "Invalid Operator"

  return result


#--------------------------------

def summation(list):
  sum = 0
  for i in list:
    sum = sum + i
  return sum

#-------------------------------

def temp_conversion(input_temp, input_scale, output_scale):
  if input_scale in ["c", "C"] and output_scale in ["F", "f"]:
    result = (input_temp * 9/5) + 32
  elif (input_scale in ["f", "F"]) and (output_scale in ["C", "c"]):
    result = (input_temp - 32) * 5/9
  elif (input_scale in ["C", "c"]) and (output_scale in ["K", "k"]):
    result = input_temp + 273
  elif (input_scale in ["K", "k"]) and (output_scale in ["C", "c"]):
    result = input_temp - 273
  elif (input_scale in ["F", "f"]) and (output_scale in ["K", "k"]):
    result = (input_temp - 32) * 5/9 + 273
  elif (input_scale in ["K", "k"]) and (output_scale in ["F", "f"]):
    result = (input_temp - 273) * 9/5 + 32
  else:
    result = "Invalid Input Unit"
  return result

#---------------------------------------

def great(list):
  maximum = list[0]
  for i in list:
    if i > maximum:
      maximum = i
  return maximum
    
#---------------------------------------

def least(list):
  minimum = list[0]
  for i in list:
    if i < minimum:
      minimum = i
  return minimum

#---------------------------------------

def table(number=2, start=1, end=10):
  for i in range(start,end+1):
    print(f"{number} x {i} = {number * i}")

