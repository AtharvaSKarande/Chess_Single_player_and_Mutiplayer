import threading
import random
import time

from Game.values.colors import CHESS_BLACK, CHESS_WHITE

class AI(threading.Thread):
    def __init__(self, ui):
        self.ui = ui
        threading.Thread.__init__(self)

    def run(self):
        if self.ui.vsAI == 'EASY':
            depth = 2
        elif self.ui.vsAI == 'MEDIUM':
            depth = 3
        elif self.ui.vsAI == 'HARD':
            depth = 4
        else:
            return
        print('Depth =', depth)
        if self.ui.aiMove is None:
            t = time.time()
            evaluation, self.ui.aiMove = self.minimax(depth, self.ui.aiColor)
            print(time.time()-t)

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
            random.shuffle(moveList)

            if len(moveList) == 0:
                board.evaluate_player_advantage()
                w, b = board.p1_adv, board.p2_adv
                isCM, isSM = board.is_checkmate(), board.draw_by_stalemate()
                if oppoColor == CHESS_BLACK:
                    if w > b:
                        if isCM:
                            maxEval = float('inf')
                    else:
                        if isSM:
                            maxEval = float('inf')
                else:
                    if b > w:
                        if isCM:
                            maxEval = float('inf')
                    else:
                        if isSM:
                            maxEval = float('inf')

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
            random.shuffle(moveList)

            if len(moveList) == 0:
                board.evaluate_player_advantage()
                w, b = board.p1_adv, board.p2_adv
                isCM, isSM = board.is_checkmate(), board.draw_by_stalemate()
                if oppoColor == CHESS_BLACK:
                    if w > b:
                        if isCM:
                            minEval = float('-inf')
                    else:
                        if isSM:
                            minEval = float('-inf')
                else:
                    if b > w:
                        if isCM:
                            minEval = float('-inf')
                    else:
                        if isSM:
                            minEval = float('-inf')

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
