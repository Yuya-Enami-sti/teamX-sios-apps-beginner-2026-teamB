import csv
from pathlib import Path

# CSVファイルにポイントカード情報を保存する
POINT_CARD_CSV = Path(__file__).with_name('point_cards.csv')


def load_point_cards() -> dict[str, dict[str, object]]:
    """CSVファイルからポイントカード情報を読み込む。"""
    point_cards: dict[str, dict[str, object]] = {}
    if not POINT_CARD_CSV.exists():
        return point_cards

    with POINT_CARD_CSV.open('r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phone = row.get('phone', '').strip()
            if not phone:
                continue

            try:
                points = int(row.get('points', '0') or '0')
            except ValueError:
                points = 0

            point_cards[phone] = {
                'name': row.get('name', '').strip(),
                'phone': phone,
                'points': points,
            }
    return point_cards


def save_point_cards(point_cards: dict[str, dict[str, object]]) -> None:
    """ポイントカード情報をCSVファイルに保存する。"""
    fieldnames = ['name', 'phone', 'points']
    with POINT_CARD_CSV.open('w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for card in point_cards.values():
            writer.writerow({
                'name': card['name'],
                'phone': card['phone'],
                'points': card['points'],
            })


def add_point_card(total_amount: int) -> tuple[int, int]:
    """ポイントカード追加機能を処理する。"""
    point_cards = load_point_cards()

    print("\n===== ポイントカード =====")
    has_card = input("ポイントカードをお持ちですか？（はい/いいえ）: ").strip().lower()

    if has_card in ['はい', 'yes', 'y']:
        phone = input("お電話番号を入力してください: ").strip()

        if phone in point_cards:
            points_earned = int(total_amount * 0.01)
            point_cards[phone]['points'] = int(point_cards[phone]['points']) + points_earned
            save_point_cards(point_cards)

            print(f"\n✓ 今回のポイント: {points_earned}ポイント")
            print(f"✓ 累積ポイント: {point_cards[phone]['points']}ポイント")
            print(f"✓ お名前: {point_cards[phone]['name']}")
            return points_earned, int(point_cards[phone]['points'])

        print("その電話番号は登録されていません。")
        return 0, 0

    name = input("お名前を入力してください: ").strip()
    phone = input("お電話番号を入力してください: ").strip()

    if phone in point_cards:
        print("その電話番号は既に登録されています。")
        return 0, int(point_cards[phone]['points'])

    points_earned = int(total_amount * 0.01)
    point_cards[phone] = {
        'name': name,
        'phone': phone,
        'points': points_earned,
    }
    save_point_cards(point_cards)

    print(f"\n✓ ポイントカードを作成しました！")
    print(f"✓ お名前: {name}")
    print(f"✓ お電話番号: {phone}")
    print(f"✓ 初期ポイント: {points_earned}ポイント")
    return points_earned, points_earned


if __name__ == '__main__':
    total_amount = 5000
    earned, total_points = add_point_card(total_amount)
    print(f'earned={earned}, total_points={total_points}')
