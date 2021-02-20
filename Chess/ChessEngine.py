"""
This class is storing all information about current state of game and valid move in current state.
"""
class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteToMove = True
        self.moving = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move so that we can undo later
        self.whiteToMove = not self.whiteToMove #Swap players

class Move():
    #Maps keys to values
    #Key : value
    ranksToRows = {"1": 7, "2": 6 , "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsTORanks = {v: k for k, v in ranksToRows.items()}
    filesTOCols = {"a": 0, "b": 1, "c": 2, "d": 3,"e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesTOCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMove = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
    def getChessNotation(self):
        return self.getRankFiles(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsTORanks[r]