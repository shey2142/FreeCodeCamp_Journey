


def arithmetic_arranger(aList, answer = False):
    arranged_problems = ''

    
    top = ""
    bottom = ""
    line = ""
    Line = ""
    result = ""
    result_1 = ""
    
    
    if len(aList) > 5:
        return "Error: Too many problems."
    for item in aList:
        operands = item.split()
        if len(operands) != 3:
            print(f"Error: Invalid item format: {item}")
        else:
            num1 = operands[0]
            operator = operands[1]
            num2 = operands[2]
            num1 = str(num1)
            num2 = str(num2)
            
            if not num1.isdigit() or not num2.isdigit():
                return "Error: Numbers must only contain digits."
  
            if operator == "+":
                try:
                    result = int(num1) + int(num2)
                    result = str(result)
                    
                except:
                    continue

            elif operator == "-":
                try:
                    result = int(num1) - int(num2)
                    result = str(result)
                    
                except:
                    continue
            else:
                
                return "Error: Operator must be '+' or '-'."
                
                
            if len(num1) > 4:
                
                return "Error: Numbers cannot be more than four digits."
                
            elif len(num2) > 4:
                
                return "Error: Numbers cannot be more than four digits."
          
            
                
            num1 = str(num1)
            num2 = str(num2)
            result = str(result)
                
            width = max(len(num1), len(num2)) + 2    
            
            num1 = num1.rjust(width)
            num2 = operator + num2.rjust(width - 1)
            line = "-" * width  
            result_1 += str(result).rjust(width) + "    "
            
            top += num1 + "    "
            bottom += num2 + "    "
            Line += str(line) + "    "
            

                  
        arranged_problems = top.rstrip() + "\n" + bottom.rstrip() + "\n" + Line.rstrip()
        
        if answer:
            arranged_problems += "\n" + result_1.rstrip()
    
                            
        
    return arranged_problems
    
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
