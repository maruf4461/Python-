#Linear forcasting modelprepare by me
x1 = float(input('Enter the Value of x1: '))
y1 = float(input('Enter the Value of y1: '))
x2 = float(input('Enter the Value of x2: '))
y2 = float(input('Enter the Value of y2: '))
slope = float((y1-y2) / (x1-x2))
c = float(y1- slope * x1)
print('Linear Equation:','y=',slope,'x +',c)
x = float(input('Enter the value of x for Forecasting: '))
y = slope * x + c
print('Forecasting for the value of x =', x,'is:',y)
