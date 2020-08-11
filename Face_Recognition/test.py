import defines

while 1:
    image = defines.capture_customer()
    groupIdList = "Customer"
    customer = defines.search_customer(image, groupIdList)
    customer_id = defines.CapCustomer.get_customer_id(customer)
    group_id = defines.CapCustomer.get_group_id(customer)

    if customer_id != 0:
        #print(user_id)
        #print(group_id)
        FaceID = defines.CapCustomer.get_cus_FaceID(customer)
        print(FaceID)

