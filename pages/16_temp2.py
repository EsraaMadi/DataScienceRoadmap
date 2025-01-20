import streamlit as st

# Initialize session state for flip state of each card
if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = [False] * 30  # 30 unique cards

# Function to toggle the flip state of a card
def flip_card(index):
    st.session_state.flipped_cards[index] = not st.session_state.flipped_cards[index]

# CSS for flip effect and styling
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
        width: 220px;
        height: 130px;
        perspective: 1000px;
        margin: 10px;
        cursor: pointer;
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
        font-size: 16px;
        font-family: 'Tajawal', sans-serif;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    .flip-card-front {
        background: #007BFF;
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

# Card data (front and back text)
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
    ("26", "وش تسمع وانت رايح الدوام"),
    ("27", "وش تسمع وانت رايح الدوام"),
    ("28", "وش تسمع وانت رايح الدوام"),
    ("29", "وش تسمع وانت رايح الدوام"),
    ("30", "وش تسمع وانت رايح الدوام"),
]

# Display cards in a grid format
for i in range(0, 30, 5):  # 5 cards per row
    cols = st.columns(5)
    for j in range(5):
        index = i + j
        if index < len(cards):
            front_text, back_text = cards[index]
            flip_class = "flipped" if st.session_state.flipped_cards[index] else ""

            # Display the flip card
            with cols[j]:
                # Create a clickable area for the card
                click_area = st.empty()
                click_area.markdown(f"""
                <div class="flip-card-container" onclick="document.getElementById('card-{index}').click()">
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

                # Hidden Streamlit button to handle clicks
                if click_area.button(f"Flip {index}", key=f"card-{index}"):
                    flip_card(index)
                    st.experimental_set_query_params()  # Triggers a rerun