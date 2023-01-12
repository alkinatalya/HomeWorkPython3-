#Вычислить число c заданной точностью d
#Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
        
number_pi = float(input('Введите число: '))
d = float(input('Введите d: '))

if d == 1:
  print(int(number_pi))
else:
    d = str(d)
    d = d.split('.') 
    d = len(d[1]) 
    print(round(number_pi, d))                              
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                