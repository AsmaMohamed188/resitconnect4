import unittest
from connect4 import setup_game,board,move,player_char, board_width,board_height

class TestConnect4(unittest,TestCase)
  def setup(self):
    setup_game # this will reset the game
  
  def test_move_places_in_column(self):
    col = 3
    move(col,player_char)
    # this will check the players is in the lowest position or not
    self.assertEqual(board[board_height -1][col], player_char)

  def test_move_doesnt_fill_ column_full(self):
    col = 2 # Going to fill column completly
    for _ in range(board_height)
        move(col,player_char)

  bottom_cell_before = board [0][col]
  move(col,player_char)
  bottom_cell_after = board[0],[col]
  self.assertEqual(bottom_cell_before,bottom_cell_after)
  