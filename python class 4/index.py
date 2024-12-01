# # Define the customers
# customer0 = {"name": "Shehroz Obaid", "lastName": "Obaid Iqbal", "age": 20, "order_price": 0}
# customer2 = {"name": "Akif Khan", "lastName": "Hanif Khan", "age": 23}
# customer3 = {"name": "Shehroz Obaid", "lastName": "Obaid Iqbal", "age": 20}
# customer4 = {"name": "Shehroz Obaid", "lastName": "Obaid Iqbal", "age": 20}

# # Put customers into a dictionary
# customers = {
#     "customer0": customer0,
#     "customer2": customer2,
#     "customer3": customer3,
#     "customer4": customer4,
# }

# # Sort the dictionary by key
# sorted_customers = dict(sorted(customers.items()))

# # Print the sorted dictionary
# print("Sorted Customers:")
# for key, value in sorted_customers.items():
#     print(f"{key}: {value}")

# # Loop through and print customer details
# print("\nCustomer Details:")
# for key, customer in sorted_customers.items():
#     for attribute, attribute_value in customer.items():
#         print(f"{attribute}: {attribute_value}")
#     print("-" * 20)


# customers_list_of_dict = {
#     "names ": ["Qasim", "Ayan", "Muhammad"],
#     "l_name": ["Hassan", "Hussain", "Uzair"],
#     "adress": ["Street786", "street787", "street788"],
#     "order_price": [120, 130, 140],
#     "order_item": ["shoes", "Shirt", "Cap"],
# }


# for keys, values in customers_list_of_dict.items():
#  print(f"{key}: {value}")    # print(keys,values)


# customers_list_of_dict = {
#     "names": ["Qasim", "Ayan", "Muhammad"],
#     "l_name": ["Hassan", "Hussain", "Uzair"],
#     "adress": ["Street786", "street787", "street788"],
#     "order_price": [120, 130, 140],
#     "order_item": ["shoes", "Shirt", "Cap"],
# }

# # Iterate over the dictionary
# for key, value in customers_list_of_dict.items():
#     print(f"{key}: {value}")

# customers_list_of_dict = {
#     "names": ["Qasim", "Ayan", "Muhammad"],
#     "l_name": ["Hassan", "Hussain", "Uzair"],
#     "adress": ["Street786", "street787", "street788"],
#     "order_price": [120, 130, 140],
#     "order_item": ["shoes", "Shirt", "Cap"],
# }

# # Convert to list of dictionaries
# customers_list = [
#     {"name": name, "l_name": l_name, "address": address, "order_price": price, "order_item": item}
#     for name, l_name, address, price, item in zip(
#         customers_list_of_dict["names"],
#         customers_list_of_dict["l_name"],
#         customers_list_of_dict["adress"],
#         customers_list_of_dict["order_price"],
#         customers_list_of_dict["order_item"],
#     )
# ]

# # Print the resulting list of dictionaries
# for customer in customers_list:
#     print(customer)


    