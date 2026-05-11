"""支払い処理とお釣りの最小枚数計算を提供するモジュール。"""

from __future__ import annotations

from typing import Dict, Sequence

DENOMINATIONS: tuple[int, ...] = (10000, 5000, 1000, 500, 100, 50, 10, 5, 1)


def calculate_change(total_amount: int, paid_amount: int, denominations: Sequence[int] = DENOMINATIONS) -> Dict[int, int]:
    """合計金額と支払金額から最小枚数のお釣りを計算する。

    Args:
        total_amount: 支払うべき合計金額（円）。
        paid_amount: 実際に支払われた金額（円）。
        denominations: 利用する貨幣の種類。

    Returns:
        各貨幣ごとの枚数を表す辞書。

    Raises:
        ValueError: 支払金額が合計金額より少ない、または負の値が入力された場合。
    """
    if total_amount < 0 or paid_amount < 0:
        raise ValueError('金額は0以上の整数で指定してください。')

    if paid_amount < total_amount:
        raise ValueError('支払金額が合計金額より少ないため、支払いを完了できません。')

    remaining_change = paid_amount - total_amount
    change: Dict[int, int] = {}

    for denomination in sorted(denominations, reverse=True):
        if remaining_change <= 0:
            break

        count, remaining_change = divmod(remaining_change, denomination)
        if count:
            change[denomination] = count

    return change


def format_change_breakdown(change: Dict[int, int]) -> str:
    """お釣りの内訳を行ごとの文字列に整形する。"""
    if not change:
        return 'お釣りはありません。'

    lines = [f'{denomination}円: {count}枚' for denomination, count in sorted(change.items(), reverse=True)]
    return '\n'.join(lines)


def read_positive_integer(prompt_text: str) -> int:
    """ユーザー入力を受け取り、正の整数として返す。"""
    raw_value = input(prompt_text).strip()
    if not raw_value.isdigit():
        raise ValueError('入力は0以上の整数でなければなりません。')

    return int(raw_value)


def read_paid_amount(total_amount: int) -> int:
    """合計金額に対して十分な支払金額をユーザーから受け取る。"""
    while True:
        try:
            paid_amount = read_positive_integer('支払金額を入力してください（円）: ')
            if paid_amount < total_amount:
                print('支払金額が合計金額より少ないです。再度入力してください。')
                continue
            return paid_amount
        except ValueError as error:
            print(f'入力エラー: {error}')


def process_payment(total_amount: int) -> None:
    """合計金額を受け取り、支払い処理を実行する。

    Args:
        total_amount: 支払うべき合計金額（円）。

    Raises:
        ValueError: 合計金額が負の値の場合。
    """
    if total_amount < 0:
        raise ValueError('合計金額は0以上の整数で指定してください。')

    print(f'合計金額: {total_amount}円')
    paid_amount = read_paid_amount(total_amount)
    change = calculate_change(total_amount, paid_amount)

    print(f'支払金額: {paid_amount}円')
    print(f'お釣り: {paid_amount - total_amount}円')
    print(format_change_breakdown(change))


def main() -> None:
    """コマンドラインから支払い処理を実行するエントリポイント（テスト用）。"""
    try:
        total_amount = read_positive_integer('合計金額を入力してください（円）: ')
        process_payment(total_amount)
    except ValueError as error:
        print(f'エラー: {error}')


if __name__ == '__main__':
    main()
