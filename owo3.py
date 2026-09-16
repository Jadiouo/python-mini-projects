import sys

# ================= 公用小工具 =================

def wait_enter():
    input("\n（按下 Enter 繼續）")


# ================= 功能 1：什麼是 VS Code？ =================

def show_intro():
    print("\n====== 1. VS Code 是什麼？ ======\n")
    print("Visual Studio Code（簡稱 VS Code）是一套免費、跨平台的程式編輯器。")
    print("特色：")
    print("  - 支援 Windows / macOS / Linux")
    print("  - 透過延伸套件（Extensions）可以支援各種語言（Python、C/C++、Web...）")
    print("  - 內建終端機、版本控制（Git），適合作為主力開發環境")
    print("  - 對初學者來說介面相對簡單，又可以慢慢變成進階 IDE")
    wait_enter()


# ================= 功能 2：安裝教學 =================

def show_installation():
    print("\n====== 2. 安裝 VS Code 步驟 ======\n")
    print("請選擇你的作業系統：")
    print("  1) Windows")
    print("  2) macOS")
    print("  3) Linux（Ubuntu 系）")

    choice = input("請輸入選項 (1/2/3)：")

    if choice == "1":
        show_install_windows()
    elif choice == "2":
        show_install_macos()
    elif choice == "3":
        show_install_linux()
    else:
        print("未選擇有效選項，回到主選單。")


def show_install_windows():
    print("\n--- Windows 安裝流程 ---\n")
    print("1. 開啟瀏覽器，搜尋：Visual Studio Code 或直接前往官網：")
    print("   https://code.visualstudio.com/")
    print("2. 頁面上點選 [Download for Windows] 下載安裝檔（.exe）。")
    print("3. 下載完成後執行安裝程式：")
    print("   - 勾選『I accept the agreement』→ Next")
    print("   - 建議勾選『Add to PATH』，這樣可以在終端機用 code 指令開啟。")
    print("   - 其他選項維持預設即可一路 Next → Install。")
    print("4. 安裝結束後啟動 VS Code。")
    print("5. 第一次開啟時，左側點選 Extensions（積木圖示），搜尋 'Python'，")
    print("   安裝由 Microsoft 提供的 Python 擴充功能。")
    print("6. 重新啟動 VS Code（或至少重開一次資料夾），就可以開始寫 Python 了！")
    wait_enter()


def show_install_macos():
    print("\n--- macOS 安裝流程 ---\n")
    print("1. 開啟瀏覽器前往 VS Code 官網：")
    print("   https://code.visualstudio.com/")
    print("2. 點選 [Download for macOS]，下載 .dmg 檔案。")
    print("3. 下載完成後，打開 .dmg，將『Visual Studio Code.app』拖曳到『Applications』資料夾。")
    print("4. 從 Launchpad 或 Finder 的『Applications』啟動 VS Code。")
    print("5. 左側 Extensions（積木圖示）搜尋 'Python'，安裝官方 Python 擴充功能。")
    print("6. 若有安裝 Homebrew，也可以在終端機輸入 `code` 開啟專案（需額外設定 PATH）。")
    wait_enter()


def show_install_linux():
    print("\n--- Linux (Ubuntu) 安裝流程 ---\n")
    print("1. 前往 VS Code 官方網站：")
    print("   https://code.visualstudio.com/")
    print("2. 下載對應發行版的安裝包，例如：")
    print("   - Ubuntu/Debian：下載 .deb 檔")
    print("3. 下載完成後，在終端機進行安裝：")
    print("   sudo dpkg -i code_xxx.deb")
    print("   若有依賴問題可以再執行：")
    print("   sudo apt-get -f install")
    print("4. 安裝完成後，在應用程式列表中找到『Visual Studio Code』啟動。")
    print("5. 開啟 VS Code 後，安裝 'Python' 擴充功能。")
    wait_enter()


# ========== 功能 3：在 VS Code 跑第一支 Python 程式 ==========

def show_python_usage():
    print("\n====== 3. 在 VS Code 執行 Python 範例 ======\n")
    print("以下示範如何在 VS Code 裡跑出『Hello, VS Code!』：\n")
    print("1. 先確認你的電腦已經安裝 Python，終端機輸入：python --version 或 python3 --version。")
    print("2. 開啟 VS Code，點選：File → Open Folder，選擇一個要放程式的資料夾。")
    print("3. 在左側 Explorer 上方，按『New File』建立新檔案，命名為 hello_vscode.py。")
    print("4. 在檔案中輸入：\n")
    print("   print('Hello, VS Code!')\n")
    print("5. 存檔之後，有兩種常見執行方式：")
    print("   (1) 按右上角的綠色 ▶ Run Python File（需安裝 Python extension）。")
    print("   (2) 使用內建終端機：")
    print("       - View → Terminal 開啟終端機")
    print("       - 在終端機輸入：python hello_vscode.py 或 python3 hello_vscode.py")
    print("6. 終端機應該會顯示：Hello, VS Code!\n")
    print("到這裡就完成你的第一支 VS Code Python 程式了 🙂")
    wait_enter()


# ========== 功能 4：個人小提醒 & 推薦設定（個人巧思） ==========

def show_tips():
    print("\n====== 4. 推薦設定與使用小撇步（個人巧思） ======\n")
    print("以下是我覺得在 VS Code 寫 Python 時很實用的小設定：\n")
    print("1. 字型大小調整：")
    print("   - 開啟 Settings（左下角齒輪 → Settings）")
    print("   - 搜尋 'font size'，將 Editor: Font Size 調成 14 ~ 16，")
    print("     對初學者來說比較不會眼花。")
    print("\n2. 主題（Theme）：")
    print("   - 在 Command Palette (Ctrl+Shift+P) 輸入 'Color Theme'")
    print("   - 可以試試『Dark+』或『Monokai』，長時間看比較舒服。")
    print("\n3. 自動存檔 Auto Save：")
    print("   - Settings 搜尋 'auto save'，選擇『afterDelay』。")
    print("   - 這樣就不會因為忘記 Ctrl+S 而跑舊版程式。")
    print("\n4. Python 相關建議：")
    print("   - 在 Extensions 安裝：Python、Pylance、Jupyter")
    print("   - 這樣會有語法高亮、即時錯誤提示，以及在 VS Code 裡跑 Jupyter Notebook 的功能。")
    print("\n5. 自己的使用心得（示範可以寫在報告裡）：")
    print("   - 一開始只用 VS Code 開單一 .py 檔熟悉介面；")
    print("   - 之後再學習如何開啟整個專案資料夾，用 Git 管理版本；")
    print("   - 最喜歡的地方是『內建終端機』，不用在視窗間切來切去。")
    wait_enter()


# ========== 功能 5：小測驗（加分巧思） ==========

def run_quiz():
    print("\n====== 5. 小測驗：你對 VS Code 了解多少？ ======\n")
    questions = [
        {
            "q": "Q1. VS Code 安裝 Python 時，最重要要裝哪一個延伸套件？",
            "options": ["A) C++", "B) Python (by Microsoft)", "C) Java", "D) LOL"],
            "ans": "b"
        },
        {
            "q": "Q2. 在 VS Code 中要打開內建終端機，常用快捷鍵是哪一組？",
            "options": ["A) Ctrl+`", "B) Ctrl+S", "C) Alt+F4", "D) Ctrl+Alt+Del"],
            "ans": "a"
        },
        {
            "q": "Q3. 若想改變編輯器字型大小，應該到哪裡調整？",
            "options": [
                "A) 左邊 Explorer",
                "B) Extensions 視窗",
                "C) Settings → Editor: Font Size",
                "D) 終端機輸入 random 指令"
            ],
            "ans": "c"
        }
    ]

    score = 0
    for item in questions:
        print(item["q"])
        for opt in item["options"]:
            print("   " + opt)
        ans = input("請輸入你的答案（a/b/c/d）：").lower().strip()
        if ans == item["ans"]:
            print("✅ 答對了！")
            score += 1
        else:
            print("❌ 答錯了～")
        print()

    print(f"測驗結束，你總共答對 {score} / {len(questions)} 題。")
    if score == len(questions):
        print("評語：你已經很了解 VS Code，可以去當同學的小老師了！")
    elif score == 0:
        print("評語：沒關係，回去再看一次安裝 & 使用說明就好～")
    else:
        print("評語：有基本概念，再多實際用幾次就會更熟。")
    wait_enter()


# ========== 主選單 ==========

def main_menu():
    while True:
        print("\n====================================")
        print("   VS Code 開發環境小幫手（Python版）")
        print("====================================")
        print("1) VS Code 是什麼？")
        print("2) 安裝 VS Code 的步驟")
        print("3) 在 VS Code 跑第一支 Python 程式")
        print("4) 推薦設定與使用小撇步（個人巧思）")
        print("5) 小測驗：檢查看懂多少")
        print("6) 離開程式")
        print("====================================")

        choice = input("請輸入選項 (1-6)：").strip()

        if choice == "1":
            show_intro()
        elif choice == "2":
            show_installation()
        elif choice == "3":
            show_python_usage()
        elif choice == "4":
            show_tips()
        elif choice == "5":
            run_quiz()
        elif choice == "6":
            print("感謝使用 VS Code 開發環境小幫手，再見～")
            sys.exit(0)
        else:
            print("無效的選項，請重新輸入。")


if __name__ == "__main__":
    main_menu()
