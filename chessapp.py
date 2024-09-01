import tkinter as tk
import chess

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess")
        self.board = chess.Board()
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.selected_piece = None
        self.valid_moves = [] 
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        piece_symbols = {
            'wK': '♔',  # White King
            'wQ': '♕',  # White Queen
            'wR': '♖',  # White Rook
            'wB': '♗',  # White Bishop
            'wN': '♘',  # White Knight
            'wP': '♙',  # White Pawn
            'bK': '♚',  # Black King
            'bQ': '♛',  # Black Queen
            'bR': '♜',  # Black Rook
            'bB': '♝',  # Black Bishop
            'bN': '♞',  # Black Knight
            'bP': '♟'   # Black Pawn
        }

        for row in range(8):
            for col in range(8):
                x0 = col * 50
                y0 = row * 50
                x1 = x0 + 50
                y1 = y0 + 50
                color = "white" if (row + col) % 2 == 0 else "gray"
                
                
                if (row, col) in self.valid_moves:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", stipple="gray25")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                
                piece = self.board.piece_at(8 * (7 - row) + col)
                if piece:
                    piece_color = 'w' if piece.color == chess.WHITE else 'b'
                    piece_key = f"{piece_color}{piece.symbol().upper()}"
                    symbol = piece_symbols.get(piece_key)
                    if symbol:
                        self.canvas.create_text(x0 + 25, y0 + 25, text=symbol, font=('Arial', 24))

    def on_click(self, event):
        col, row = event.x // 50, event.y // 50
        square = 8 * (7 - row) + col
        piece = self.board.piece_at(square)

        if self.selected_piece:
            from_square = self.selected_piece
            to_square = square
            move = chess.Move(from_square, to_square)
            if move in self.board.legal_moves:
                self.board.push(move)
            self.selected_piece = None
            self.valid_moves = []  # Limpiar movimientos válidos
            self.draw_board()
        else:
            if piece:
                self.selected_piece = square
                self.valid_moves = self.get_valid_moves(square)
                self.draw_board()

    def get_valid_moves(self, square):
        moves = []
        piece = self.board.piece_at(square)
        piece_color = chess.WHITE if piece.color == chess.WHITE else chess.BLACK
        for move in self.board.legal_moves:
            if move.from_square == square:
                to_row, to_col = 7 - (move.to_square // 8), move.to_square % 8
                moves.append((to_row, to_col))
        return moves

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
