shopping_cart = []
          
class ShoppingCart:
    def __init__(self, addItem, removeItem, calculateCost = 0):
        self.additem = addItem
        self.removeitem = removeItem
        self.calculatecost = calculateCost
        self.additem = []

    def add_item(self):
        item = (item)
        self.additem += item
        self.additem.append(item)
        print('Successful')

        
    def remove_item():
        item_name = input('Enter item name to be removed: ')
        item_name.removeItem.remove(shopping_cart)

    def cal_total():
        print()


def main():
    shopping_cart = []

    while True:
        print("""
                press 1 to add item to cart
                press 2 to remove item from cart
                press 3 to calculate cost of item
                press 4 to exit
                """)
        resp = input('Press a number: ')
        if resp == '1':
            item_name = input('Enter item name: ')
            item_price = input('Enter item price: ')
            new_item = ShoppingCart(item_name, item_price)
            shopping_cart.append(new_item)
        elif resp == '2':
        #     item_name = input('Enter item to be removed: ')
        #     if len(shopping_cart) >= 1:
        #         for item in shopping_cart:
        #             if item.additem == item_name:
        #                 item.add_item
        #                 break
        #             else:
        #                 print('No item')
        #         else:
        #             print('Could not find item')
        #     else:
        #         print('No item found')
        # elif resp == '3':
        #     costTotal = 0
        #     while len(shopping_cart) >= costTotal:
        #         print(f'The total cost is {shopping_cart}')
        #         break
        elif resp == '4':
            break

main()