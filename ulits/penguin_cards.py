import streamlit as st
import ulits.load_data as ld


@st.cache_data(show_spinner="Fetching roadmap...")
def _get_raw_card():
    df = ld.load_esraa_cards()
    return df

# Function to toggle flip state for a specific card
def flip_card(index):
    st.session_state.flipped_cards[index] = not st.session_state.flipped_cards[index]





# CSS for flip effect and styling
flip_css = """
<style>
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
    }
    .flip-card-front {
        background: #d8d9da;
    }
    .flip-card-front img {
        width: 100%; /* Adjusted to fit the card */
        height: 100%;
        object-fit: cover; /* Ensures image covers the entire card */
        border-radius: 12px;
    }
    .flip-card-back {
        background: #d8d9da;
        transform: rotateY(180deg);
    }
</style>
"""

def get_cards():

    df_cards = _get_raw_card()
    # Initialize session state for flip state of each card
    if "flipped_cards" not in st.session_state:
        st.session_state.flipped_cards = [i==1 for i in list(df_cards['Status'])]  # 7 unique cards

    st.markdown(flip_css, unsafe_allow_html=True)

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
                            </div>
                            <div class="flip-card-back"></div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
