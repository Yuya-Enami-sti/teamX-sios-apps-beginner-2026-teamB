from src.bill import items
from src.order import calculate_total, Order, read_orders
from src.payment import calculate_change, format_change_breakdown
from src.PointFunction import add_point_card


def print_product_list() -> None:
    print('=== 商品一覧 ===')
    for item in items:
        print(f"{item['name']} - {item['price']}円 (在庫: {item['stock']})")


def print_order_summary(orders: list[Order]) -> None:
    print('\n=== 注文内容 ===')
    for order in orders:
        print(f"{order.product_name} x {order.number_of_purchases}")


def read_payment_amount(total_amount: int) -> int:
    while True:
        raw_value = input(f'支払金額を入力してください（合計 {total_amount}円）: ').strip()
        if not raw_value.isdigit():
            print('数値を入力してください。')
            continue
        payment = int(raw_value)
        if payment < total_amount:
            print('支払金額が不足しています。')
            continue
        return payment


def main() -> None:
    print('ようこそ、お会計アプリへ！')
    print_product_list()

    orders = read_orders()
    if not orders:
        print('\n注文がありませんでした。終了します。')
        return

    total_amount = calculate_total(orders)
    print_order_summary(orders)
    print(f'合計金額: {total_amount}円')

    points_earned, total_points = add_point_card(total_amount)
    print(f'付与ポイント: {points_earned}pt')
    if total_points:
        print(f'現在の累積ポイント: {total_points}pt')

    payment = read_payment_amount(total_amount)
    change = calculate_change(total_amount, payment)

    print(f'\n支払金額: {payment}円')
    print(f'お釣り: {payment - total_amount}円')
    print(format_change_breakdown(change))
    print('\n=== ありがとうございました ===')


if __name__ == '__main__':
    main()
