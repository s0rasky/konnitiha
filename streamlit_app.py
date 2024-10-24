
import streamlit as st
import random

def generate_workout(focus, distance):
    warmup = ["400m イージー", "200m キック", "200m プル"]
    
    main_set = {
        "プル": [
            "8 x 50m パドルプル",
            "4 x 100m プル",
            "3 x 200m プルネガティブ "
        ],
        "キック": [
            "8 x 50m ボードキック ",
            "4 x 100m グライドキック",
            "3 x 200m IMキック"
        ],
        "スイム": [
            "8 x 50m ドリルスイム",
            "4 x 100m IM",
            "3 x 200m ディセンディング"
        ]
    }
    
    distance_set = {
        "短距離": [
            "10 x 25m スプリント",
            "5 x 50m ハード",
            "3 x 75m ビルドアップ"
        ],
        "長距離": [
            "1 x 400m ディスタンス",
            "2 x 300m ネガティブ",
            "3 x 200m IM"
        ]
    }
    
    cooldown = ["200m イージー", "100m S1"]
    
    workout = random.choice(warmup) + "\n\n"
    workout += "Main Set:\n"
    workout += "\n".join(random.sample(main_set[focus], 2)) + "\n\n"
    workout += "Distance Set:\n"
    workout += random.choice(distance_set[distance]) + "\n\n"
    workout += random.choice(cooldown)
    
    return workout

st.title("水泳練習メニュー生成器")

focus = st.selectbox("鍛えたい能力を選択してください:", ["プル", "キック", "スイム"])
distance = st.selectbox("泳ぐ距離を選択してください:", ["短距離", "長距離"])

if st.button("練習メニューを生成"):
    workout = generate_workout(focus, distance)
    st.text_area("あなたの練習メニュー:", workout, height=300)
