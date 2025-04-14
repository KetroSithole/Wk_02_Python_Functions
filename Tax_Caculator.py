Tax=0.15
Uif=0.01
Gross_Salary=0

def Tax_Calculator(Gross_Salary):
    Net_Income=Gross_Salary-(Tax*Gross_Salary)-(Uif*Gross_Salary)
    return (Net_Income)


print(Tax_Calculator(15000))
