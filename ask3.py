#ΔΗΜΙΟΥΡΓΙΑ ΛΙΣΤΑΣ ΜΕ ΤΟΥΣ ΣΥΝΔΥΑΣΜΟΥΣ
def toString(List): 
    return ''.join(List) 
  
# ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΠΑΡΑΓΕΙ ΤΟΥΣ ΣΥΝΔΥΑΣΜΟΥΣ ΑΠΟ ΤΗ ΛΕΞΗ ΠΟΥ ΔΙΝΩ
# Οι 3 παράμετροι μου είναι: 
# 1. Ενα string
# 2. Αρχη του string
# 3. Τέλος του string. 
def permute_fun(a, s, e): 
    if s == e: 
        print(toString(a) )
    else: 
        for i in range(s, e + 1): 
            a[s], a[i] = a[i], a[s] 
            permute_fun(a, s + 1, e) 
            a[s], a[i] = a[i], a[s] # backtrack 
  
# To πρόγραμμα καλει την συνάρτηση permute για τη λέξη
# που θα δώσω από την κονσόλα
my_start_word = input('Δώσε μία λέξη: ')
n = len(my_start_word) 
a = list(my_start_word) 
permute_fun(a, 0, n-1) 
  
# This code is contributed by Bhavya Jain 