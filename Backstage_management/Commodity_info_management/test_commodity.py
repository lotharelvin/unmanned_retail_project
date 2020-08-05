import commodity_model as commodity

com1=commodity.Commodity(1,20,156,1,'Cigarette')
com1.myprint()
print('\n')
New_ID=2
New_price=21
Incre=100
Decre=1
New_Shelf=2
New_Type='Alcohol'

com1.Change_ID(New_ID)
com1.myprint()
print('\n')

com1.Change_Price(New_price)
com1.myprint()
print('\n')

com1.Add_Inventory(Incre)
com1.myprint()
print('\n')

com1.Dec_Inventory(Decre)
com1.myprint()
print('\n')

com1.Change_Shelf(New_Shelf)
com1.myprint()
print('\n')

com1.Change_Type(New_Type)
com1.myprint()
print('\n')

com1.Reset()
com1.myprint()
print('\n')
