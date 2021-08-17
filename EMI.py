#Write program to calculate monthly simple interest and compound interest (5% monthly) on amount 161258

a=161258
e3=a/36
e5=a/60
emi3=e3+(0.05*e3)
emi5=e5+(0.05*e3)
print("EMI for 3 years with interest 5%",emi3)
print("EMi for 5 years with interest 5%",emi5)