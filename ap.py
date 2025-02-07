import streamlit as st
import numpy as np

class TeamworkStrategyGame:
    def __init__(self, players):
        self.players = players
        self.board = self.initialize_board()
        self.turn = 0

    def initialize_board(self):
        return [['-' for _ in range(5)] for _ in range(5)]

    def display_board(self):
        return '\n'.join([' '.join(row) for row in self.board])

    def take_turn(self, player, x, y, action):
        if self.board[x][y] != '-':
            return "Invalid move! Space occupied."
        self.board[x][y] = action
        self.next_turn()
        return f"{player} performed {action} at ({x}, {y})"

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

# Streamlit UI
def main():
    st.title("Teamwork Strategy Game")
    players = ["Alice", "Bob"]
    game = TeamworkStrategyGame(players)
    
    if 'game' not in st.session_state:
        st.session_state['game'] = game
    
    st.write("Current Board:")
    st.text(st.session_state['game'].display_board())
    
    player = players[st.session_state['game'].turn]
    st.write(f"Current Turn: {player}")
    
    x = st.number_input("Enter X coordinate:", min_value=0, max_value=4, step=1)
    y = st.number_input("Enter Y coordinate:", min_value=0, max_value=4, step=1)
    action = st.selectbox("Select Action:", ["Build", "Defend"])
    
    if st.button("Take Turn"):
        result = st.session_state['game'].take_turn(player, x, y, action)
        st.write(result)
        st.write("Updated Board:")
        st.text(st.session_state['game'].display_board())

if __name__ == "__main__":
    main()
