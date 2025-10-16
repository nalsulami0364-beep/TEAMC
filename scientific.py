import math
functions= ["sin^-1", "sin-1", "asin","log","cos^-1", 
            "cos-1", "acos","tan^-1", "tan-1", "atan",
            "csc-1","csc^-1","acsc","sec-1","sec^-1","asec","cot-1","cot^-1","acot"
            "log10","e","e^","exp","exponential","factorial","n!"
            ,"sin","cos","tan","csc","sec","cot","sinh","cosh","tanh","csch","sech","coth"]
def main_scientific_menu(): 
    while True:
        typeOfFunction= input("Enter function: ").lower().strip()
        if typeOfFunction in functions:
            break
        else: print("error ---> Invalid function name or unspported function")
    if typeOfFunction not in["sin^-1", "sin-1", "asin","log","cos^-1", 
            "cos-1", "acos","tan^-1", "tan-1", "atan",
            "log10","e","e^","exp","exponential","factorial","n!"]:
        while True:
            typeofAngel= input("Degree or radian? ").lower().strip()
            if typeofAngel in["degree",  "radian"]:
                break
            else: print("Error choose between --> Degree or radian")
    else: typeofAngel= None
    while True:
        valuestr = input("Enter value: ")
        try:
            value1 = eval(valuestr, {"pi": math.pi, "Pi": math.pi,"3.14": math.pi})
            if typeofAngel=="radian":
                if ("pi" not in valuestr.lower() and "3.14" not in valuestr.lower()):
                    print("Error --> in radian you can use pi for \"example: pi/3\"")
                    continue
            break
        except:
            print("Error --> in radian you can use pi for \"example: pi/3\"")
    return typeOfFunction, typeofAngel, value1,valuestr
def toRadians(value,typeofAngel):
        if typeofAngel== None:
            return value
        elif typeofAngel== "degree":
            value= math.radians(value)
            return value
        elif typeofAngel== "radian":
            return value


def function(typeOfFunction,value):
    Result=None
    try:
        if typeOfFunction == "sin":
            Result= math.sin(value)
            
        elif typeOfFunction == "cos":
            Result= math.cos(value)
            
        elif typeOfFunction == "tan":
            Result= math.tan(value) 

        #--------------
        elif typeOfFunction == "csc":
            try:
                Result = 1 / math.sin(value) 
            except ZeroDivisionError:
                print("Zero Division Error")
                 
        elif typeOfFunction == "sec":
            try:
                Result = 1 / math.cos(value)
            except ZeroDivisionError:
                print("Zero Division Error")
             
        elif typeOfFunction == "cot":
            try:
                Result = 1 / math.tan(value)
            except ZeroDivisionError:
                print("Zero Division Error")
             
        #------------- 
        elif typeOfFunction in ["sin^-1", "sin-1", "asin"] and -1<=value<=1:
            try:
                Result = math.asin(value)
                Result = math.degrees(Result)
            except: print("value should be between 1 and -1 ")
            
        elif typeOfFunction in ["cos^-1", "cos-1", "acos"] and -1<=value<=1:
            try:
                Result = math.acos(value)
                Result = math.degrees(Result)
            except: print("value should be between 1 and -1 ")
            
        elif typeOfFunction in ["tan^-1", "tan-1", "atan"]:
            Result = math.atan(value)
            Result = math.degrees(Result)
        elif typeOfFunction in ["csc-1","csc^-1","acsc"] and (value>=1 or value <=-1):
            try:
                Result = math.asin(1/value) 
            except ZeroDivisionError:
                print("Zero Division Error")
            except: print("value should be higher than 1 or lower than -1 ")
                 
        elif typeOfFunction in ["sec-1","sec^-1","asec"] and (value>=1 or value <=-1):
            try:
                Result = math.acos(1/value) 
            except ZeroDivisionError:
                print("Zero Division Error")
            except: print("value should be higher than 1 or lower than -1 ")
             
        elif typeOfFunction in ["cot-1","cot^-1","acot"]:
            try:
                Result = math.atan(1/value) 
            except ZeroDivisionError:
                print("Zero Division Error")
        #---------------
        elif typeOfFunction == "sinh":
            Result = math.sinh(value)
            
        elif typeOfFunction == "cosh":
            Result = math.cosh(value)
            
        elif typeOfFunction == "tanh":
            Result = math.tanh(value)

        elif typeOfFunction == "csch":
            try:
                Result = 1 / math.sinh(value) 
            except ZeroDivisionError:
                print("Zero Division Error")
                 
        elif typeOfFunction == "sech":
            try:
                Result = 1 / math.cosh(value)
            except ZeroDivisionError:
                print("Zero Division Error")
             
        elif typeOfFunction == "coth":
            try:
                Result = 1 / math.tanh(value)
            except ZeroDivisionError:
                print("Zero Division Error")
            
        # -------------
        elif typeOfFunction == "log10":
            try:
                if value>0:
                    Result = math.log10(value)
            except ValueError: print("must be float or int") 
            except: print("Domain error happen")
            
        elif typeOfFunction == "log":
            base= (input("What is the base of log? if you want to make it ln(x) enter --> e: "))
            if base== "e":
                base= 2.718281828459045
            try:
                if value>0:
                    Result = math.log(value,float(base))
            except ValueError: print("must be float or int")
        #-----------------
        elif typeOfFunction in["e","e^","exp","exponential"]:
            Result = math.exp(value)
        elif typeOfFunction in ["factorial","n!"]:
            if value>0 and value==int(value) :
                Result = math.factorial(value)
            else: print("The value of factorial must be positive integr")
    except: print(" error ")
    return Result
def scientific_menu():
    typeOfFunction, typeofAngel, value1, valuestr = main_scientific_menu()
    value = toRadians(value1, typeofAngel)
    result = function(typeOfFunction,value)

    if result is not None:
        if result < -1e16 or result > 1e16:
            result = "complex number (Infinity)"
        elif isinstance(result, float):
            result = round(result, 3)
    print("\nResult of",typeOfFunction,"(",valuestr,")  is: ", result)

# #_______________________________________________________________________________________
# import math

# def scientific_menu():
#     typeOfFunction = input("Enter function: ").lower().strip()
#     if typeOfFunction not in ["sin^-1", "sin-1", "asin","log","cos^-1",
#             "cos-1", "acos","tan^-1", "tan-1", "atan",
#             "log10","e","e^","exp","exponential","factorial","n!"]:
#         while True:
#             typeofAngel = input("Degree or radian? ").lower().strip()
#             if typeofAngel in ["degree", "radian"]:
#                 break
#             else:
#                 print("Error choose between --> Degree or radian")
#     else:
#         typeofAngel = None

#     # خذ القيمة من المستخدم داخل نفس الدالة
#     valuestr = input("Enter value: ")
#     value1 = eval(valuestr, {"pi": math.pi , "Pi": math.pi})

#     # حوّلها حسب الزاوية
#     value = toRadians(value1, typeofAngel)

#     # نفّذ العملية
#     result = function(typeOfFunction, value)

#     # اطبع النتيجة
#     if result is None:
#         print("Invalid input or domain error.")
#     elif isinstance(result, float):
#         result = round(result, 3)
#     elif result > 1e16 or result < -1e16:
#         result = "complex number (Infinity)"
#     print(f"Result of {typeOfFunction} ({valuestr}) is: {result}")


# def toRadians(value, typeofAngel):
#     if typeofAngel == "degree":
#         return math.radians(value)
#     return value


# def function(typeOfFunction, value):
#     try:
#         if typeOfFunction == "sin":
#             return math.sin(value)
#         elif typeOfFunction == "cos":
#             return math.cos(value)
#         elif typeOfFunction == "tan":
#             return math.tan(value)
#         elif typeOfFunction == "log10":
#             return math.log10(value)
#         elif typeOfFunction in ["e", "e^", "exp", "exponential"]:
#             return math.exp(value)
#         elif typeOfFunction in ["factorial", "n!"]:
#             return math.factorial(int(value))
#         else:
#             print("Unsupported function.")
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None
