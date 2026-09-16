import random
import sys


# ====== Game 1：終極密碼・東海版 ======
def game_guess_number():
    print("\n===== 遊戲一：終極密碼・東海版 =====")
    print("在東海校園裡，有一個神秘彩蛋藏在某個『編號』裡。")
    print("請先選擇難度：")
    print("1) 簡單：1~50，有 10 次機會")
    print("2) 普通：1~100，有 8 次機會")
    print("3) 困難：1~200，有 7 次機會")

    # 選擇難度
    while True:
        level = input("請輸入難度 (1/2/3)：")
        if level == "1":
            low, high, chances = 1, 50, 10
            break
        elif level == "2":
            low, high, chances = 1, 100, 8
            break
        elif level == "3":
            low, high, chances = 1, 200, 7
            break
        else:
            print("輸入錯誤，請重新選擇 1 / 2 / 3。")

    answer = random.randint(low, high)
    guess_count = 0

    print(f"\n彩蛋藏在 {low} ~ {high} 之間的某一個數字。")
    print(f"你共有 {chances} 次機會，祝你好運！")

    while chances > 0:
        print(f"\n目前可猜範圍：{low} ~ {high}")
        print(f"剩餘次數：{chances}")

        user_input = input("請輸入你的猜測（或輸入 q 離開遊戲）：")
        if user_input.lower() == "q":
            print("你選擇離開遊戲，彩蛋就留在校園某處吧XD")
            return

        try:
            guess = int(user_input)
        except ValueError:
            print("請輸入『整數』！")
            continue

        if guess < low or guess > high:
            print("超出目前提示範圍了，再想想！")
            continue

        guess_count += 1
        chances -= 1

        if guess == answer:
            print("\n✅ 恭喜你找到彩蛋！")
            print(f"正確答案是：{answer}")
            print(f"你總共猜了 {guess_count} 次。")

            # 評價系統
            if guess_count <= 3:
                print("評價：東海導覽小天才！你一定很熟校園～")
            elif guess_count <= 8:
                print("評價：合格的東海人，下次可以挑戰更困難！")
            else:
                print("評價：你可能是沿路邊走邊滑手機才會迷路吧 XD")
            return
        elif guess < answer:
            print("太小了！彩蛋在更大的編號。")
            low = max(low, guess + 1)
        else:
            print("太大了！彩蛋在更小的編號。")
            high = min(high, guess - 1)

    # 機會用完
    print("\n😵 次數用完啦！")
    print(f"正確答案其實是 {answer}。")
    print("下次再來校園尋寶吧～")


# ====== Game 2：東海夜跑生存戰 ======
def game_night_run():
    print("\n===== 遊戲二：東海夜跑生存戰 =====")
    print("故事：你晚上在東海校園夜跑，目標是在體力耗盡前跑到『東海教堂』。")
    print("每一回合會發生隨機事件，你可以選擇：衝刺 / 穩穩跑 / 休息。")
    print("當距離 <= 0 代表抵達教堂；當體力 <= 0 代表累癱失敗。")

    # 初始狀態
    distance = 10.0   # 距離教堂 10 格
    energy = 100      # 體力
    fat_penalty = 0   # 喝飲料之後每回合額外扣的體力

    # 隨機事件列表
    events = [
        {
            "name": "牧場微風",
            "desc": "你路過牧場，牛在旁邊安靜看著你，心情放鬆。",
            "delta_energy": +5,
            "delta_distance": 0,
            "effect": "none"
        },
        {
            "name": "上坡地獄",
            "desc": "前方突然是一段上坡，你不得不加把勁往上跑。",
            "delta_energy": -10,
            "delta_distance": -0.5,
            "effect": "none"
        },
        {
            "name": "飲料誘惑",
            "desc": "同學揪你停下來喝手搖飲，你考慮了一下...",
            "delta_energy": 0,
            "delta_distance": 0,
            "effect": "drink_choice"
        },
        {
            "name": "路燈昏暗",
            "desc": "路燈有點暗，你下意識放慢速度，小心翼翼前進。",
            "delta_energy": -5,
            "delta_distance": 0,
            "effect": "none"
        },
        {
            "name": "人超多的路段",
            "desc": "前方人好多，你不好意思停下來，只好假裝很專業地跑過去。",
            "delta_energy": -5,
            "delta_distance": -0.5,
            "effect": "force_run_fast"
        },
    ]

    round_count = 0

    while distance > 0 and energy > 0:
        round_count += 1
        print("\n-----------------------------")
        print(f"第 {round_count} 回合")
        print(f"距離教堂剩下：{distance:.1f} 格")
        print(f"目前體力：{energy} 點（額外體力負擔：{fat_penalty}）")

        # 觸發隨機事件
        event = random.choice(events)
        print(f"\n【隨機事件：{event['name']}】")
        print(event["desc"])

        forced_action = None

        if event["effect"] == "drink_choice":
            # 問玩家要不要喝
            while True:
                drink = input("要跟同學一起喝飲料嗎？(y/n)：").lower()
                if drink == "y":
                    print("你選擇喝飲料，當下精神有回來一點，但之後每回合會多扣體力。")
                    energy += 15
                    fat_penalty += 5
                    break
                elif drink == "n":
                    print("你拒絕了飲料誘惑，繼續堅持夜跑。")
                    break
                else:
                    print("請輸入 y 或 n。")
        elif event["effect"] == "force_run_fast":
            print("因為人太多，你不好意思停下來休息，這回合被迫衝刺！")
            forced_action = "1"

        # 套用事件本身的影響
        energy += event["delta_energy"]
        distance += event["delta_distance"]

        # 檢查事件後是否已經倒下或到達終點
        if energy <= 0 or distance <= 0:
            break

        # 玩家選擇行動
        print("\n請選擇你的行動：")
        print("1) 衝刺跑：距離 -2 格，體力 -25")
        print("2) 穩穩跑：距離 -1 格，體力 -15")
        print("3) 慢慢走順便滑手機：距離 -0.5 格，體力 -5")

        while True:
            if forced_action is not None:
                action = forced_action
                print(f"(本回合強制行動：{action})")
            else:
                action = input("請輸入 1 / 2 / 3：")

            if action == "1":
                distance -= 2
                energy -= 25 + fat_penalty
                break
            elif action == "2":
                distance -= 1
                energy -= 15 + fat_penalty
                break
            elif action == "3":
                distance -= 0.5
                energy -= 5 + fat_penalty
                break
            else:
                print("輸入錯誤，請重新輸入 1 / 2 / 3。")
                if forced_action is not None:
                    # 理論上不會發生，但保險起見
                    forced_action = None

    # 遊戲結局
    print("\n=======================")
    if distance <= 0 and energy > 0:
        print("🎉 你順利抵達東海教堂！")
        print(f"共花了 {round_count} 回合。")
        if energy > 30:
            print("你還有力氣拍 IG 限時動態，配上夜景超漂亮！")
        else:
            print("你坐在教堂前喘得像狗，但至少成功了！")
    elif energy <= 0 and distance > 0:
        print("💀 你體力耗盡，倒在半路上。")
        print(f"距離教堂還剩 {distance:.1f} 格。")
        print("路過的學長把你撿起來，順便跟你說：『下次白天再跑啦』。")
    else:
        # 同時 <= 0 的極端情況
        print("你在最後一口氣衝到教堂門口，倒下去的同時完成任務。")
        print("這畫面會成為你大學的傳說。")


# ====== 主選單 ======
def main_menu():
    while True:
        print("\n==============================")
        print("歡迎來到 Python 小遊戲集合")
        print("1) 終極密碼・東海版")
        print("2) 東海夜跑生存戰")
        print("3) 離開")
        print("==============================")

        choice = input("請選擇要玩的遊戲 (1/2/3)：")

        if choice == "1":
            game_guess_number()
        elif choice == "2":
            game_night_run()
        elif choice == "3":
            print("感謝遊玩，掰掰～")
            sys.exit(0)
        else:
            print("輸入錯誤，請重新輸入 1 / 2 / 3。")


if __name__ == "__main__":
    main_menu()
