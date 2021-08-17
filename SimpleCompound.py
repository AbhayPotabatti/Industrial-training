#Write program to calculate monthly simple interest  and compound interest (5% monthly) on amount - 161258

p=161258
r=5
t=1

si=p*r*t/100
print("si is:",si)

Amount = p*(pow((1+r/100),t))
ci = Amount - p
print("Compount interest is ",ci)
