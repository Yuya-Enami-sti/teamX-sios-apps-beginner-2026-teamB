import bill

def is_valid_product_name(product_name):
    return next((item for item in bill.items if item['name'] == product_name), None) is not None

class Order:
    def __init__(self, product_name, number_of_purchases):
        self.product_name = product_name
        self.number_of_purchases = number_of_purchases

order_list = []

while True:
    while True:
        product_name = input("商品名を入力してください")
        if not is_valid_product_name(product_name):
            print("正しい商品名を入力してください")
        else:
            order_list.append(Order(product_name, number_of_purchases))
            break

    while True:
        number_of_purchases = input("購入数を入力してください")
        if not number_of_purchases.isdigit() or int(number_of_purchases) <= 0:
            print("正しい数値を入力してください")
        else:
            break

    print("注文を続けますか？")
    answer = input("y/n: ")
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("正しい入力をしてください")

print("注文内容:")

for order in order_list:
    print(f"商品名: {order.product_name}, 購入数: {order.number_of_purchases}")

total_cost = sum(order.number_of_purchases for order in order_list)
print(f"合計金額: {total_cost}")






if __name__ == '__main__':
    print('商品注文システム作成')