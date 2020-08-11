import defines

while 1:
    image = defines.capture_customer()
    groupIdList = "Customer"
    customer = defines.search_customer(image, groupIdList)
    user_id = defines.CapCustomer.get_user_id(customer)
    group_id = defines.CapCustomer.get_group_id(customer)

    if user_id != 0:
        print(user_id)
        print(group_id)

