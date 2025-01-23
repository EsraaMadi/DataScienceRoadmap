import streamlit as st

# Initialize session state for flip state of each card
if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = [False] * 7  # 7 unique cards

# Function to toggle flip state for a specific card
def flip_card(index):
    st.session_state.flipped_cards[index] = not st.session_state.flipped_cards[index]

# CSS for flip effect and styling
flip_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    .flip-card-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .flip-card {
        background-color: transparent;
        width: 5.0cm;
        height: 7.1cm;
        perspective: 800px;
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
        border-radius: 14px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        top: 0;
        left: 0;
    }
    .flip-card-front {
        background: #d8d9da;
        position: absolute;
        overflow: hidden;
    }
    .flip-card-front img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 12px;
    }
    .flip-card-front .overlay-text {
        position: absolute;
        bottom: 10%; /* Adjust as needed for spacing from the bottom */
        left: 50%;
        transform: translateX(-50%);
        font-size: 2rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
        text-align: center;
    }
    .flip-card-back {
    background: #d8d9da;
    transform: rotateY(180deg);
    font-weight: bold;
    color: #333;
    text-align: center;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* Ensures top, center, and bottom text are spaced */
    }

    .flip-card-back .top-text {
    font-size: 1.5rem;
    margin: 18px 0;
    font-family: 'Tajawal', sans-serif;
    }

    .flip-card-back .center-text {
    font-size: 3rem;
    margin: 15px 0; /* Adds some spacing */
    }

    .flip-card-back .bottom-text {
    font-size: 1rem;
    }

</style>
"""
st.markdown(flip_css, unsafe_allow_html=True)

# Define numbers for front and texts for back
card_numbers = [1, 2, 3, 4, 5, 6, 7]
top_texts = [
    "عبدالرحمن المقاطي",
    "Esraa",
    "Esraa",
    "Esraa",
    "Esraa",
    "Esraa",
    "Esraa",
]
center_texts = [
    "🧊",
    "🧊",
    "🧊",
    "🧊",
    "🧊",
    "🧊",
    "🧊",
]
bottom_texts = [
    "2025/2/16",
    "Date",
    "Date",
    "Date",
    "Date",
    "Date",
    "Date",
]

# Display up to 3 Cards per Row
for row in range(0, 7, 3):  # 3 cards per row
    cols = st.columns(min(3, 7 - row))  # Ensures the last row has the correct number of cards
    for i in range(min(3, 7 - row)):
        index = row + i
        flip_class = "flipped" if st.session_state.flipped_cards[index] else ""

        with cols[i]:
            st.markdown(f"""
            <div class="flip-card-container">
                <div class="flip-card {flip_class}">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <img src='https://i.ibb.co/fHr4Qdb/Penguin-of-the-week-back-1-removebg-preview.png' alt='Card Image'>
                            <div class="overlay-text">{card_numbers[index]}</div>
                        </div>
                        <div class="flip-card-back">
                            <div class="top-text">{top_texts[index]}</div>
                            <div class="center-text">{center_texts[index]}</div>
                            <div class="bottom-text">Expire at: {bottom_texts[index]}</div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Button to flip the card
            if st.button(f"🧊 Flip Card {index+1} 🧊", key=f"btn_{index}"):
                flip_card(index)
                st.rerun()  # Forces UI update to reflect state changes