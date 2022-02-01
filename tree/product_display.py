def display_organizer(products):
    for product in products:
        if product["type"]:
            print(f"""For product {product["name"]}:
             We have the following price(s):
                NEW: {product['new']}
                RESEALED: {product['resealed']}
            And the following description:
                '{product['desc']}'    
            """)

        else:
            print(f"""For product {product["name"]}:
            We have the following price(s):
                NEW: {product['new']}   
            """)
