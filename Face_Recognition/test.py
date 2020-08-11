import defines

image = defines.capture_customer()
customer = defines.search_customer(image)
user_id = defines.CapCustomer.get_user_id(customer)
group_id = defines.CapCustomer.get_group_id(customer)

print(user_id)
print("    ")
print(group_id)