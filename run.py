import Main_Copy as main
import Sel_ as sel
import pandas as pd

p = main.Scrape()
k = input("Are you a Child? Y/N")
if k == "Y" or k =="y" :
    age = "child"
else:
    age = "adult"
c= p.Age(age)
m = 1
dis = {}
print("Choose your symptoms number : ")
print("\n")
for i,j in c.items() :
    print( m , " = ", i)
    dis.update({m : i})
    m += 1
print("From 1 to ", m-1)

s= int(input("Choose your general symptom : "))
p.Symptom_View(c)
l = p.Get_Symptom_Link(dis[s], c)
#l = p.Get_Symptom_Link("Abdominal pain in children", c)
print(c)
print(dis[s])
print(l[0])
print("Choose your symptoms with comma: ")
print("\n")
ino = 1
disk = {}
for i,j in l[0].items():
    print(i)
    for k in j :
        print(ino ," = ",k )
        disk.update({ino : k})
        ino += 1


#print(s[1])
#print("\n")
#print(s[0])

print("\n")

k = sel.FormSubmit()
lst = ["main_0_maincontent_1_QualifierRepeater_FactorRepeater_0_CheckBoxQualifier_0", "main_0_maincontent_1_QualifierRepeater_FactorRepeater_4_CheckBoxQualifier_6"]
#k.Checkbox_select("main_0_maincontent_1_QualifierRepeater_FactorRepeater_0_CheckBoxQualifier_0","FindCause")
j = k.Checkbox_select(lst,"FindCause")

#k.Get_Final_Diagnosis(j)