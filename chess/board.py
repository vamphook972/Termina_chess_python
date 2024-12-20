class board:
    def __init__(self):
        self.board = self.start_board()

    def start_board(self):
        return [
            ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"],
            ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"],
            ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"],
            ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"],
            ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"],
            ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"],
            ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"],
            ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"],
        ]

    def show_board(self):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        print("""
                |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
        """)
        for i in range(8):
            print(f"""
            {letters[i]} |  {self.board[i]}
            """)
