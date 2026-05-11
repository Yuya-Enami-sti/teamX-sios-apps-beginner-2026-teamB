# ポイントカード追加機能
point_cards = {}  # ポイントカード情報を保存する辞書

def add_point_card(total_amount):
    """ポイントカード追加機能を処理する"""
    
    print("\n===== ポイントカード =====")
    has_card = input("ポイントカードをお持ちですか？（はい/いいえ）: ").strip()
    
    if has_card in ['はい', 'yes', 'y']:
        # 既存のポイントカード
        phone = input("お電話番号を入力してください: ").strip()
        
        if phone in point_cards:
            # ポイント付与
            points_earned = int(total_amount * 0.01)  # 合計金額の1%
            point_cards[phone]['points'] += points_earned
            
            print(f"\n✓ 今回のポイント: {points_earned}ポイント")
            print(f"✓ 累積ポイント: {point_cards[phone]['points']}ポイント")
            print(f"✓ お名前: {point_cards[phone]['name']}")
            
            return points_earned, point_cards[phone]['points']
        else:
            print("その電話番号は登録されていません。")
            return 0, 0
    
    else:
        # 新規ポイントカード作成
        name = input("お名前を入力してください: ").strip()
        phone = input("お電話番号を入力してください: ").strip()
        
        if phone in point_cards:
            print("その電話番号は既に登録されています。")
            return 0, 0
        
        # ポイントカード作成
        points_ = int(total_amount * 0.01)  # 合計金額の1%
        point_cards[phone] = {
            'name': name,
            'phone': phone,
            'points': points_earned
        }
    
        
        print(f"\n✓ ポイントカードを作成しました！")
        print(f"✓ お名前: {name}")
        print(f"✓ お電話番号: {phone}")
        print(f"✓ 保持ポイント: {points_earned}ポイント")
        
        return points_earned, points_earned

if __name__ == '__main__':
    # テスト用
    total_amount = 5000
    earned, total_points = add_point_card(total_amount)
