# Plan
# Create testcases for the following function
# # display_board
# # switch_player_turn
# # get_player_move
# # check_for_win
# # play_game

import unittest

from game import switch_player_turn

class TestGame(unittest.TestCase):

    def test_switch_player_turn(self):
        self.assertEqual(switch_player_turn('player1'), 'player2')

if __name__ == '__main__':
    unittest.main()