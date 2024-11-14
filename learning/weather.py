def weather(temperature):
    if temperature <= 0:
        return("it's cold outside")
    elif 0 <= temperature <= 15:
        return("It's chilly outside")
    elif 16 <= temperature <= 25:
        return("it's warm outsite")
    else:
        return("it's hot outside")
    
print(weather(-2))
print(weather(10))
print(weather(31))