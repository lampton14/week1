Unit = input("please input Custormary or Metric: ")
if Unit == "Customary":
    value = input("what is your weight in pounds?")
    value2 = input("what is your height in inches?")
    value= float(value)
    value2= float(value2)
    BMI = 703*value/value2**2

if Unit == "Metric":
    value3 = input("what is your weight in kilos?")
    value4 = input("what is your height in meters?")
    value3 = float(value3)
    value4 = float(value4)
    BMI = value3/value4**2

print(str(BMI))
if (BMI) > 20 and BMI < 25:
    print("you are healthy")
if (BMI) <20:
    print("you are underweight")
if (BMI) >25:
    print("you are overweight")
