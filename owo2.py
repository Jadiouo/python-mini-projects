import sys

import cv2
import numpy as np


def cartoonize(img, k=8):
    """
    把一般照片轉成類似繪本 / 卡通風格的圖片
    步驟：
    1. 用雙邊濾波讓顏色變平滑但保留邊緣
    2. 做邊緣偵測，產生黑色線稿
    3. 顏色做 K-means 量化，讓色塊更「塊狀」
    4. 把線稿疊回色塊上
    """

    # 1) 雙邊濾波：柔化顏色但保留邊緣
    color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 2) 邊緣偵測：做成像漫畫線稿一樣
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9, 2
    )
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # 3) 顏色量化：用 K-means 把顏色變成少數幾種「色塊」
    data = color.reshape((-1, 3))
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(
        data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()].reshape(color.shape)

    # 4) 線稿 & 色塊混合：讓邊緣變得比較明顯
    cartoon = cv2.bitwise_and(quantized, edges_color)

    return cartoon


def add_storybook_frame(img, title="Donghai Chapel Story"):
    """
    在圖片外加一圈「書頁」邊框 + 標題文字，讓它更像繪本的一頁
    """
    h, w = img.shape[:2]

    # 建立比原圖稍大的底圖當「紙張」
    margin = 40
    page_color = (245, 245, 230)  # 淺米色像紙
    page = np.full((h + margin * 2, w + margin * 2, 3), page_color, dtype=np.uint8)

    # 把圖貼到中間
    page[margin:margin + h, margin:margin + w] = img

    # 畫外框線
    cv2.rectangle(
        page,
        (margin - 5, margin - 5),
        (margin + w + 5, margin + h + 5),
        (180, 180, 160),
        2
    )

    # 標題文字
    cv2.putText(
        page,
        title,
        (margin, margin - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (80, 80, 60),
        2,
        cv2.LINE_AA
    )

    return page


def main():
    # 預設用同目錄的 sample.jpg（程式產生的示意圖），也可以用命令列指定自己的照片：
    #   python owo2.py my_photo.jpg
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.jpg"
    img = cv2.imread(path)

    if img is None:
        print(f"讀不到圖片檔案：{path}，請確認檔名與路徑是否正確")
        return

    # 讓圖片寬度差不多固定，避免太大
    max_width = 800
    h, w = img.shape[:2]
    if w > max_width:
        scale = max_width / w
        img = cv2.resize(img, (max_width, int(h * scale)), interpolation=cv2.INTER_AREA)

    # 做成繪本 / 卡通風格
    cartoon = cartoonize(img, k=8)

    # 加上「繪本頁」邊框
    cartoon_page = add_storybook_frame(cartoon, title="Donghai Chapel Story")

    # 把原圖也縮成類似風格的頁面，方便左右對比
    original_page = add_storybook_frame(img, title="Original Photo")

    # 左右拼在一起顯示：左原圖、右繪本風格
    both = np.hstack((original_page, cartoon_page))

    cv2.imshow("Donghai Chapel - Storybook Style (S=Save, Q=Quit)", both)

    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q') or key == 27:
            break
        elif key == ord('s'):
            cv2.imwrite("chapel_storybook.png", both)
            print("已將結果存成 chapel_storybook.png")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
