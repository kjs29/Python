word = "python"
print(word[2:4])        #this will print th, which is characters from position 0 (included) to 4(excluded)

---

word = "python"
print(word[2:])         #this will print characters from position 2(included) to the end

---

word = "python"
print(word[:2])         #this will print characters from the beginning position to 2(excluded)

---

#this also makes sure that word[:2] + word[2:] is always equal to word
word = "python"
print(word[:2]+word[2:])  #python

---

a = "1234567Rainy"
print(a[1:-1:2]) #[1(included position):-1(excluded position):2(interval)]

result : 
'''
^   ^   ^   ^   ^ 
2 3 4 5 6 7 R a i n y
'''
246Ri
