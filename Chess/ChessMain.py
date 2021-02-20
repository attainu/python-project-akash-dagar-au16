import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Initialize a global directory of images.
"""
def loadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wR", "wN", "wB", "wQ", "wK", "bp", "wp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelcted = () #it will keep track of the last click of the user (tuple: (row, col))
    playerClicks = [] #keep track of player clicks
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelcted == (row, col):
                    sqSelcted == ()
                    playerClicks == ()
                else:
                    sqSelcted = (row, col)
                    playerClicks.append(sqSelcted)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    #print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelcted = ()
                    playerClicks = []


        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


        """
        Responsible for all the graphics with in a current game state.
        """

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


    """
    Draw squares on the board.
    """
def drawBoard(screen):
    colors = [p.Color("white"),p.Color("grey")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col)% 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE,SQ_SIZE,SQ_SIZE))


    """
    Draw the pieces on board using the current GameState.board
    """

def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE,SQ_SIZE))


if __name__ == '__main__':
    main()