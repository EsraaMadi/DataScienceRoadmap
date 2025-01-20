import streamlit as st
import time

import random

students = list(range(0, 25))

# Shuffle the student numbers randomly
random.shuffle(students)

# Flip the next card automatically every second
def auto_flip():
    current_card = students[st.session_state.current_card]
    #print(st.session_state.current_card,students[st.session_state.current_card])
    st.session_state.flipped_cards[current_card] = not st.session_state.flipped_cards[current_card]
    st.session_state.current_card += 1



def drow_cards():
    # Initialize session state for flip state of each card and the current flip index
    if "flipped_cards" not in st.session_state:
        st.session_state.flipped_cards = [False] * len(students)  # 25 unique cards
    if "current_card" not in st.session_state:
        st.session_state.current_card = 0  # Start with the first card
    
    # CSS for flip effect and spacing with background image fix
    flip_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
        /* Background Image for the Streamlit App */
        .stApp {
            background-image: url('https://i.pinimg.com/736x/45/f5/eb/45f5eb7f27b9101c490401259672ad0a.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
    
        .flip-card-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .flip-card {
            background-color: transparent;
            width: 220px; /* Wider Cards */
            height: 130px;
            perspective: 1000px;
            margin: 10px; /* Adds spacing between cards */
            cursor: pointer; /* Clickable */
        }
        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }
        .flipped .flip-card-inner {
            transform: rotateY(180deg);
        }
        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 16px; /* Smaller Font */
            font-family: 'Tajawal', sans-serif; /* Arabic Font */
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        .flip-card-front {
            background-image: url("https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg");
            color: white;
        }
        .flip-card-back {
            background: #FFD700;
            color: black;
            transform: rotateY(180deg);
        }
    </style>
    """
    st.markdown(flip_css, unsafe_allow_html=True)
    
    # List of card texts for front and back
    cards = [
        ("1", "وش تسمع وانت رايح الدوام؟"),
        ("2", "وش تسمع وانت رايح الدوام"),
        ("3", "وش تسمع وانت رايح الدوام"),
        ("4", "وش تسمع وانت رايح الدوام"),
        ("5", "وش تسمع وانت رايح الدوام"),
        ("6", "وش تسمع وانت رايح الدوام"),
        ("7", "وش تسمع وانت رايح الدوام"),
        ("8", "وش تسمع وانت رايح الدوام"),
        ("9", "وش تسمع وانت رايح الدوام"),
        ("10", "وش تسمع وانت رايح الدوام"),
        ("11", "وش تسمع وانت رايح الدوام"),
        ("12", "وش تسمع وانت رايح الدوام"),
        ("13", "وش تسمع وانت رايح الدوام"),
        ("14", "وش تسمع وانت رايح الدوام"),
        ("15", "وش تسمع وانت رايح الدوام"),
        ("16", "وش تسمع وانت رايح الدوام"),
        ("17", "وش تسمع وانت رايح الدوام"),
        ("18", "وش تسمع وانت رايح الدوام"),
        ("19", "وش تسمع وانت رايح الدوام"),
        ("20", "وش تسمع وانت رايح الدوام"),
        ("21", "وش تسمع وانت رايح الدوام"),
        ("22", "وش تسمع وانت رايح الدوام"),
        ("23", "وش تسمع وانت رايح الدوام"),
        ("24", "وش تسمع وانت رايح الدوام"),
        ("25", "وش تسمع وانت رايح الدوام"),
    ]
    

    # Trigger the automatic flip
    auto_flip()
    #time.sleep(1)  # Wait for 1 second
    
    # Display Cards in Rows with Proper Margins
    for i in range(0, len(students), 5):  # 5 cards per row
        cols = st.columns(5)
        for j in range(5):
            index = i + j
            if index < len(cards):
                front_text, back_text = cards[index]
                flip_class = "flipped" if st.session_state.flipped_cards[index] else ""
    
                # Display Flip Card inside a container for spacing
                with cols[j]:
                    st.markdown(f"""
                    <div class="flip-card-container">
                        <div class="flip-card {flip_class}">
                            <div class="flip-card-inner">
                                <div class="flip-card-front">
                                    {front_text}
                                </div>
                                <div class="flip-card-back">
                                    {back_text}
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    if st.session_state.current_card < len(students):
        # Rerun the Streamlit app to continuously update the UI
        st.rerun()