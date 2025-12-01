pdt1= int(input("Enter product Price"))
pdt2= int(input("Enter product Price"))
pdt3= int(input("Enter product Price"))
pdt4= int(input("Enter product Price"))

Total= pdt1+pdt2+pdt3+pdt4
print ("Total Product Priece=", Total)

GST= Total * (18/100)
print ("GST Amount=", GST)

Tax= Total +  GST
print ("Total tax to pay=", Tax)