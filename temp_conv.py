# Temperature convertor

Type_c_f=input ("Choose F for Fahrenheit or C for Celcius:")
Temp=float (input ("Enter temperature:"))

def Temp_c(Temp):
    result_f = (Temp - 32) * (5/9)
    return result_f

def Temp_f(Temp):
    result_c = (1.8 * Temp) + 32
    return result_c

if Type_c_f.lower() == "f":
    print ("The result in F is:", Temp_c(Temp))
else:
    print ("The result in F is:", Temp_f(Temp))


