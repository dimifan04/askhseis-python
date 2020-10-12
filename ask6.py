import numpy as np

#x = np.random.randint(2, size=(10, 10))
#print(x)

# Πρέπει να διαβάζουμε 0 ή 1
# Μετά να το βάζουμε σε πίνακα με δισδιάστατο με διπλά for
# Κάθε φορά που βάζουμε έναν αριθμό τσεκάρουμε:
# 1. αν ειναι 0 
# 2. αν είναι 1
# 3. ανάλογα με την επιλογή αυξάνουμε count_0 ή count_1
# 4. Aν αυξήσω το count_0 μηδενίζω το count_1
# 5. Οταν βρώ 4 συνεχόμενα (count_0 = 4 ή count_1 = 4) ΣΤΑΜΑΤΩ
# 6. Αν βρω 5 συνεχόμενα δημιουργώ μόνο μία 4αδα με τα 4 πρώτα

n = 10
a = [[0] * n for i in range(n)]
count_0 = 0
count_1 = 0
number_counter = 0
i = 1
while i < 10:
    j = 1
    while j < 10:
            a[i][j] = np.random.randint(2) # ενα ενα τα στοιχεια (0 ή 1)
            number_counter = number_counter + 1
            if a[i][j] == 0:
                count_0 = count_0 + 1
                count_1 = 0
                if count_0 == 4:
                    print("ΣΥΝΕΧΟΜΕΝΑ 4 ΜΗΔΕΝΙΚΑ")
                    break;
            elif a[i][j] == 1:
                count_1 = count_1 + 1
                count_0 = 0
                if count_1 == 4:
                    print("ΣΥΝΕΧΟΜΕΝΟΙ 4 ΑΣΣΟΙ")
                    break
            j = j +1
    
    if a[i][i] == 0: # ΚΥΡΙΑ ΔΙΑΓΩΝΙΟΣ
       count_0 = count_0 + 1
       count_1 = 0
       if count_0 == 4:
           print("ΣΥΝΕΧΟΜΕΝΑ 4 ΜΗΔΕΝΙΚΑ ΣΤΗΝ ΚΥΡΙΑ ΔΙΑΓΩΝΙΟ")
           break
       elif a[i][i] == 1: # ΚΥΡΙΑ ΔΙΑΓΩΝΙΟΣ
          count_1 = count_1 + 1
          count_0 = 0
          if count_1 == 4:
             print("ΣΥΝΕΧΟΜΕΝΟΙ 4 ΑΣΣΟΙ ΣΤΗΝ ΚΥΡΙΑ ΔΙΑΓΩΝΙΟ")
             break            
    i = i + 1

#EKTYΠΩΝΩ ΤΗΝ ΜΟΡΦΗ ΤΟΥ ΤΕΛΙΚΟΥ ΠΙΝΑΚΑ
for row in a:
    print(' '.join([str(elem) for elem in row]))

print('ΧΡΕΙΑΣΤΗΚΑΝ : ',number_counter,' ΑΡΙΘΜΟΙ')