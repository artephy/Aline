ON_SIZE = 30
OFF_SIZE = 30
INPUT_SIZE = 255       # Input integer size
OUTPUT_SIZE = 255      # Output integer size
INT_TYPE = 'const uint8_t'
TABLE_NAME = 'light0_lookUp';

def cie1931(L):
    L = L*100.0
    if L <= 8:
        return (L/902.3)
    else:
        return ((L+16.0)/116.0)**3

x = range(0,int(INPUT_SIZE-ON_SIZE-OFF_SIZE+1))
y = [round(cie1931(float(L)/len(x))*OUTPUT_SIZE) for L in x]

y = [0]*OFF_SIZE+y+[255]*ON_SIZE
#for i in range(len(y)):
#	y[i]=255-y[i]

f = open('cie1931.h', 'w')
f.write('// CIE1931 correction table\n')
f.write('// Automatically generated\n\n')

f.write('%s %s[%d] PROGMEM = {\n' % (INT_TYPE, TABLE_NAME, len(y)))
f.write('\t')
for L in y:
    f.write('%d, ' % int(L))
f.write('\n};\n\n')