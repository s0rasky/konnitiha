python
import streamlit as st
import random

def generate_workout(focus, distance):
    warmup = ["400m easy swim", "200m kick", "200m pull"]
    
    main_set = {
        "プル": [
            "8 x 50m pull with paddles",
            "4 x 100m pull with buoy",
            "3 x 200m pull negative split"
        ],
        "キック": [
            "8 x 50m kick with board",
            "4 x 100m kick without board",
            "3 x 200m IM kick (50 each stroke)"
        ],
        "スイム": [
            "8 x 50m drill/swim",
            "4 x 100m IM",
            "3 x 200m freestyle with descending pace"
        ]
    }
    
    distance_set = {
        "短距離": [
            "10 x 25m sprints",
            "5 x 50m at race pace",
            "3 x 75m build"
        ],
        "長距離": [
            "1 x 400m steady pace",
            "2 x 300m negative split",
            "3 x 200m with 20 sec rest"
        ]
    }
    
    cooldown = ["200m easy swim", "100m choice stroke", "100m backstroke"]
    
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
