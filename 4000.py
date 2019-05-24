import sys
sys.path.extend(['./src'])

from pygomoku.Board import Board
from pygomoku.Player import HumanPlayer, PureMCTSPlayer
from pygomoku.GameServer import GameServer

def run():
    board = Board(width=9, height=9)
    player1 = PureMCTSPlayer(Board.kPlayerBlack, name="AI 1",weight_c=5, compute_budget=4000)
    # player1 = HumanPlayer(Board.kPlayerBlack, name="player 1")

    player2 = PureMCTSPlayer(Board.kPlayerWhite, name="AI 2", weight_c=5, compute_budget=10000)
    # player2 = HumanPlayer(Board.kPlayerWhite, name="player 2")

    server = GameServer(board, GameServer.kNormalPlayGame, player1, player2)
    server.startGame()

if __name__ == '__main__':
    for _ in range(30):
        run()
