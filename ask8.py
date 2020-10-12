import numpy as np

# υποθέτω οτι ειμαι σε ορθογώνιο σύστημα αξόνων και φτιάχνω
# τις αντίστοιχες συντεταγμένες - κινήσεις
#-1,1    0,1    1,1
#-1,0    0,0    0,1
#-1,-1   0,-1   1,-1


s = 0
n  = 100
x = 0
y = 0

for i in range(n):
        giro = 0
        while (giro == 0):
            a = np.random.randint(1,5)
            #print('a = ', a)
            if a==1:
                y = y + 1
                s = s + y
            elif a == 2:
                y = y - 1
                s = s + y
            elif a == 3:
                x = x + 1
                s = s + x
            elif a == 4:
                x = x - 1
                s = s + x
            #print('x = ',x)
            #print('y = ',y)
            if x==0 and y==0:
                print('ZEROS')
                giro = 1
                x = 0
                y = 0
                break
     #   if x==0 and y==0:
     #       break
        
mo = s/n
print('MO = ',mo)