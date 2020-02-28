a=2  
with open(('1.md'), 'r',encoding='UTF-8') as f:
    for line in f:
        for ch in line:
            if ch=='$':
                if a % 2 == 0:
                    ch='[latex]'
                    a = a + 1
                elif a % 2 != 0:
                    ch = '[/latex]'
                    a = a + 1
            print (ch,end='')
