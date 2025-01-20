import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Flip Cards App", layout="centered")

# HTML, CSS, and JavaScript for the flip cards
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin: 0;
            padding: 0;
        }
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            justify-items: center;
            margin-top: 50px;
            width: 100%;
            max-width: 800px;
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
</head>
<body>
    <div class="cards-container">
        <!-- Cards will be dynamically generated here -->
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">Alex</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">Bella</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">Chris</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">Dana</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">Eli</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">Faye</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
        <div class="flip-card" onclick="this.classList.toggle('flipped')">
            <div class="flip-card-inner">
                <div class="flip-card-front">George</div>
                <div class="flip-card-back" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/32/Emperor_Penguin_chick_%28cropped%29.jpg');"></div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render the HTML in the Streamlit app
st.components.v1.html(html_code, height=500)