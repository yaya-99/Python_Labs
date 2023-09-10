reply = int(input('do you want the metric system or pound and iches? choose 1 or 2: '))
if reply == 1:
    w= float(input('enter weight in kg: '))
    h = float(input('enter height in m: '))
    b = w/(h)**2
    print(' Your BMI is ',b)
elif reply ==2:
    W = float(input('enter weight in pounds: '))
    H = float(input('enter height in inches: '))
    B = (W*0.453)/(H*0.0254)**2
    print('Your BMI is ',B)
else:
    print('invalid output.')
