import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Flip Cards App", layout="centered")

# Add custom CSS and JavaScript for flip cards
custom_css = """
    <style>
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            justify-items: center;
            margin-top: 50px;
        }
        .flip-card {
            background-color: transparent;
            width: 150px;
            height: 200px;
            perspective: 1000px;
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
        .flip-card.flipped .flip-card-inner {
            transform: rotateY(180deg);
        }
        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
            border-radius: 10px;
            overflow: hidden;
        }
        .flip-card-front {
            background-color: #007bff;
            color: white;
            font-size: 18px;
            font-weight: bold;
        }
        .flip-card-back {
            background-color: #fff;
            background-size: cover;
            background-position: center;
        }
    </style>
"""

custom_js = """
    <script>
        const cards = document.querySelectorAll('.flip-card');
        cards.forEach(card => {
            card.addEventListener('click', () => {
                card.classList.toggle('flipped');
            });
        });
    </script>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Generate the flip cards with random names on the front and a penguin image on the back
names = ["Alex", "Bella", "Chris", "Dana", "Eli", "Faye", "George"]
image_url = "https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg"  # Publicly available penguin image

# HTML structure for the flip cards
cards_html = '<div class="cards-container">'
for name in names:
    card_html = f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">{name}</div>
                <div class="flip-card-back" style="background-image: url('{image_url}');"></div>
            </div>
        </div>
    """
    cards_html += card_html
cards_html += "</div>"

# Display the cards
st.markdown(cards_html, unsafe_allow_html=True)

# Inject the JavaScript for interactivity
st.markdown(custom_js, unsafe_allow_html=True)