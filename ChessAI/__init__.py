import threading
from Game.values.colors import CHESS_BLACK, CHESS_WHITE

class AI(threading.Thread):
    def __init__(self, ui):
        self.ui = ui
        threading.Thread.__init__(self)

    def run(self):
        if self.ui.aiMove is None:
            evaluation, self.ui.aiMove = self.minimax(3, self.ui.aiColor)

    def minimax(self, depth, aiColor, alpha=float('-inf'), beta=float('inf')):
        board = self.ui.chessBoard
        if depth == 0:
            return board.evaluate_advantage(self.ui.aiColor), None

        if aiColor == self.ui.aiColor:

            oppoColor = CHESS_WHITE
            if aiColor == CHESS_WHITE:
                oppoColor = CHESS_BLACK

            maxEval = float('-inf')
            best_move = None
            moveList = board.get_all_valid_moves(aiColor)

            for mv in moveList:
                board.move(mv, debug=True)
                evaluation, bstMoveTillNow = self.minimax(depth-1, oppoColor, alpha, beta)
                board.move_back(debug=True)
                maxEval = max(maxEval, evaluation)
                if maxEval == evaluation:
                    best_move = mv
                alpha = max(alpha, evaluation)
                if beta < alpha:
                    return maxEval, best_move
            return maxEval, best_move

        else:
            oppoColor = CHESS_WHITE
            if aiColor == CHESS_WHITE:
                oppoColor = CHESS_BLACK

            minEval = float('inf')
            best_move = None
            moveList = board.get_all_valid_moves(aiColor)

            for mv in moveList:
                board.move(mv, debug=True)
                evaluation, bstMoveTillNow = self.minimax(depth - 1, oppoColor, alpha, beta)
                board.move_back(debug=True)
                minEval = min(minEval, evaluation)
                if minEval == evaluation:
                    best_move = mv
                beta = min(beta, evaluation)
                if beta < alpha:
                    return minEval, best_move
            return minEval, best_move
