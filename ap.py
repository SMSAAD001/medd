import streamlit as st
import random

def main():
    st.title("Number Guessing Game")
    
    if 'random_number' not in st.session_state:
        st.session_state.random_number = random.randint(1, 100)
    
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    
    st.write("Guess a number between 1 and 100")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Check Guess") and not st.session_state.game_over:
        if guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.success("Congratulations! You guessed the correct number.")
            st.session_state.game_over = True
            
    if st.button("Restart Game"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.game_over = False
        st.experimental_rerun()

if __name__ == "__main__":
    main()
