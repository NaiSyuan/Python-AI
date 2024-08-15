import streamlit as st
import os
import time


# 載入指定資料夾中的圖片檔案
def load_images(folder):
    return [f for f in os.listdir(folder) if f.endswith((".jpg", ".png"))]


# 初始化商品資訊
def initialize_commodity(image_folder, img_files):
    if "commodity" not in st.session_state:
        # 為每個圖片檔案創建一個商品項目
        st.session_state.commodity = {
            img[:-4]: {  # 使用檔案名(不含副檔名)作為商品名稱
                "price": 10,  # 初始價格
                "stock": 10,  # 初始庫存
                "image": f"{image_folder}/{img}",  # 圖片路徑
            }
            for img in img_files
        }


# 顯示商品
def display_products(cols):
    for i, (item_name, item_info) in enumerate(st.session_state.commodity.items()):
        with cols[i % len(cols)]:  # 使用模運算來決定商品顯示在哪一列
            st.image(item_info["image"], use_column_width=True)
            st.subheader(item_name)
            st.write(f"價格: {item_info['price']}")
            st.write(f"庫存: {item_info['stock']}")

            # 購買按鈕
            if st.button(f"購買{item_name}", key=f"buy_{item_name}"):
                if item_info["stock"] > 0:
                    st.session_state.commodity[item_name]["stock"] -= 1
                    # [item_name] 是商品名稱的變數，它對應於 commodity 字典中的一個具體鍵。這樣做的好處是可以動態地訪問不同商品的庫存。
                    # "stock"這是字典中的一個具體屬性，代表該商品的庫存數量。
                    st.success(f"購買{item_name}成功")
                    time.sleep(0.5)
                    st.rerun()  # 重新載入頁面以更新顯示
                else:
                    st.error(f"購買{item_name}失敗")


# 新增商品庫存
def add_stock():
    st.title("新增商品庫存")
    product_name = st.selectbox(
        "請選擇要補貨的商品", list(st.session_state.commodity.keys())
    )
    add = st.number_input(
        "請輸入要新增的庫存數量", value=1, min_value=1, max_value=10, step=1
    )
    if st.button("新增庫存"):
        st.session_state.commodity[product_name]["stock"] += add  # 新增庫存，
        st.success("新增庫存成功")
        time.sleep(0.5)
        st.rerun()  # 重新載入頁面以更新顯示


# 顯示當前庫存
def display_current_stock():
    st.write("目前庫存")
    for item_name, item_info in st.session_state.commodity.items():
        st.write(f"{item_name}: {item_info['stock']}")


# 主函數
def main():
    st.title("Vegeterian 購物商城")

    # 讓用戶選擇顯示的列數
    columns = st.number_input("請輸入行數", value=1, min_value=1, max_value=10, step=1)
    cols = st.columns(columns)

    # 設定圖片資料夾和載入圖片
    image_folder = "image"
    img_files = load_images(image_folder)

    # 初始化商品資訊
    initialize_commodity(image_folder, img_files)

    # 顯示商品
    display_products(cols)

    # 新增庫存功能
    add_stock()

    # 顯示當前庫存
    display_current_stock()


# 程式入口點
if __name__ == "__main__":
    main()
