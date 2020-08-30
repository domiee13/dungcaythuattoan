# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



# Example

# For cell = "a1", the output should be
# chessKnightMoves(cell) = 2.



# For cell = "c2", the output should be
# chessKnightMoves(cell) = 6.

def chessKnightMoves(cell):
    
    def isValid(pos):
        if 0 <= pos and pos < 8:
            return True
        return False

    def getX(pos):
        return ord(pos) - ord('a')

    def getY(pos):
        return ord(pos) - ord('1')

    current_x = getX(cell[0])
    current_y = getY(cell[1])
    result = 0

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx * dy) == 2:
                if isValid(current_x + dx) and isValid(current_y + dy):
                    result += 1
    return result
