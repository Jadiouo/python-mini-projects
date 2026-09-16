# python-mini-projects

幾個 Python 小練習：OpenCV 影像風格化，加上終端機小遊戲 / 教學程式。

| 檔案 | 說明 | 需要的套件 |
|---|---|---|
| `owo2.py` | 把照片轉成繪本 / 卡通風格：雙邊濾波 → 自適應閾值邊緣線稿 → K-means 色彩量化 → 疊圖 → 加故事書外框。預設讀 `sample.jpg`，也可 `python owo2.py 自己的照片.jpg`；視窗中按 `S` 存檔、`Q` 離開 | opencv-python、numpy |
| `sample.jpg` | 程式畫出來的示意場景（教堂、樹、雲），用來測試 `owo2.py` | — |
| `owo.py` | 終端機小遊戲集：「終極密碼・東海版」猜數字、「東海夜跑生存戰」文字冒險 | 無 |
| `owo3.py` | 「什麼是 VS Code？」互動式教學 CLI：介紹、各平台安裝步驟、Python 使用方式、小技巧與測驗 | 無 |

倒單擺控制模擬已獨立成 [inverted-pendulum-control](https://github.com/Jadiouo/inverted-pendulum-control)。

## 執行

```bash
pip install -r requirements.txt
python owo2.py              # 或 python owo2.py my_photo.jpg
python owo.py
python owo3.py
```

## 授權

MIT
