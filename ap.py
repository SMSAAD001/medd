import streamlit as st
import random
import time

# Initialize game state
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.character_y = 200
    st.session_state.food_x = random.randint(50, 350)
    st.session_state.food_y = random.randint(50, 350)
    st.session_state.jump = False

def jump():
    st.session_state.jump = True

def reset():
    st.session_state.score = 0
    st.session_state.character_y = 200
    st.session_state.food_x = random.randint(50, 350)
    st.session_state.food_y = random.randint(50, 350)
    st.session_state.jump = False

st.title("Jump and Eat Game")
st.write(f"Score: {st.session_state.score}")

# Jump button
if st.button("Jump"):
    jump()

# Game loop
if st.session_state.jump:
    st.session_state.character_y -= 50  # Move up
    time.sleep(0.2)
    st.session_state.character_y += 50  # Move down
    st.session_state.jump = False

# Check if character reaches food
if abs(st.session_state.character_y - st.session_state.food_y) < 30 and abs(200 - st.session_state.food_x) < 30:
    st.session_state.score += 1
    st.session_state.food_x = random.randint(50, 350)
    st.session_state.food_y = random.randint(50, 350)

# Render game
st.write(f"Character Y: {st.session_state.character_y}")
st.write(f"Food Position: ({st.session_state.food_x}, {st.session_state.food_y})")

# Reset button
if st.button("Reset Game"):
    reset()
