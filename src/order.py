from dataclasses import dataclass
from typing import List

try:
    from . import bill
except ImportError:
    import bill


@dataclass
class Order:
    product_name: str
    number_of_purchases: int


def is_valid_product_name(product_name: str) -> bool:
    return next((item for item in bill.items if item['name'] == product_name), None) is not None


def read_positive_integer(prompt_text: str) -> int:
    while True:
        raw_value = input(prompt_text).strip()
        if raw_value.isdigit() and int(raw_value) > 0:
            return int(raw_value)
        print('正しい数値を入力してください。')


def read_orders() -> List[Order]:
    orders: List[Order] = []
    while True:
        product_name = input('商品名を入力してください: ').strip()
        if not is_valid_product_name(product_name):
            print('正しい商品名を入力してください')
            continue

        number_of_purchases = read_positive_integer('購入数を入力してください: ')
        orders.append(Order(product_name=product_name, number_of_purchases=number_of_purchases))

        answer = input('注文を続けますか？ (y/n): ').strip().lower()
        if answer == 'n':
            break
        if answer != 'y':
            print('無効な入力です。注文を終了します。')
            break

    return orders


def calculate_total(orders: List[Order]) -> int:
    total = 0
    for order in orders:
        item = next(item for item in bill.items if item['name'] == order.product_name)
        total += item['price'] * order.number_of_purchases
    return total


if __name__ == '__main__':
    print('商品注文システム作成')
