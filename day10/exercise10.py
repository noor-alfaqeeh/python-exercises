print('..........exercise1.........')
import sympy as sym
from sympy import  cos, sin, exp, tan
from sympy.plotting import plot
from sympy.plotting import plot3d

x,y,i,n,z = sym.symbols('x y i n z')
expr = x**2+x**3+21*x**4+10*x+1
print ( expr.subs(x, 7) )

print(sym.expand( (x + y) ** 2 ))

print( sym.simplify(4*x**3+21*x**2+10*x+12))

print(sym.limit(1/(x**2),x,sym.oo))

print(sym.summation(2*i +i-1, (i, 5, n)))

print( sym.integrate(sin(x)+exp(x)*cos(x)+tan(x),x))

print( sym.factor(x**3+12*x*y*z+3*y**2*z) )

print( sym.solveset(x - 4, x))

m1 = sym.Matrix([[5,12,40], [30,70,2]])
m2= sym.Matrix([2, 1, 0])
print( m1*m2 )

plot(x**3+3, (x, -10, 10))

f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))

print('..........exercise2.........')
import xlsxwriter
workbook = xlsxwriter.Workbook('Noor.xlsx')
worksheet = workbook.add_worksheet()
data=['This is Example','My fist export example',1,2,3]
format1=workbook.add_format({'bold':True, 'font_color':'red','font_size':20})
format2=workbook.add_format({'font_size':20})
worksheet.set_column('A:A', 20)
worksheet.write('A1', data[0],format1)
worksheet.write('A2', data[1], format2)
for x in range(2):
    worksheet.write(x+2, 0, x+1)
worksheet.write('A5', data[4],format1)
workbook.close()


print('..........exercise3.........')
from xlrd import open_workbook
wb = open_workbook('Noor2.xlsx')
for s in wb.sheets():
    print ("Sheet:", s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
    print()

        
        
