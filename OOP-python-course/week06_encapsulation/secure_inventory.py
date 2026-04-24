class Product_FGA:
    def __init__(self_FGA, name_FGA, price_FGA, quantity_FGA):
        self_FGA.__name_FGA = name_FGA
        self_FGA.__price_FGA = price_FGA
        self_FGA.__quantity_FGA = quantity_FGA

    def get_product_info_FGA(self_FGA):
        print("Product:", self_FGA.__name_FGA)
        print("Price:", self_FGA.__price_FGA)
        print("Quantity:", self_FGA.__quantity_FGA)

    def update_quantity_FGA(self_FGA, new_quantity_FGA):
        if new_quantity_FGA >= 0:
            self_FGA.__quantity_FGA = new_quantity_FGA

    def update_price_FGA(self_FGA, new_price_FGA):
        if new_price_FGA > 0:
            self_FGA.__price_FGA = new_price_FGA

# Example usage
product_FGA = Product_FGA("Laptop", 45000, 10)
product_FGA.get_product_info_FGA()

