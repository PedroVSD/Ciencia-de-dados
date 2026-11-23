import random

class Sudoku:
    N = 9
    EMPTY = 0

    def main(self):
        board = self.generate_random_sudoku()
        print("Tabuleiro de Sudoku gerado aleatoriamente:")
        self.print_board(board)

        print("Tente resolver o Sudoku. Use números de 1 a 9 e 0 para células vazias.")

        if self.solve_sudoku(board):
            print("\nParabéns! Você resolveu o Sudoku!")
        else:
            print("\nNão foi possível resolver o Sudoku gerado. Mais sorte na próxima vez!")

    def solve_sudoku(self, board):
        scanner = Scanner()

        while not self.is_solved(board):
            row = scanner.input_int("\nDigite a linha (de 1 a 9) da célula que deseja alterar: ", 1, 9) - 1
            col = scanner.input_int("Digite a coluna (de 1 a 9) da célula que deseja alterar: ", 1, 9) - 1

            if row < 0 or row >= self.N or col < 0 or col >= self.N or board[row][col] != self.EMPTY:
                print("Célula inválida ou já preenchida. Tente novamente.")
                continue

            num = scanner.input_int(f"Insira um número para a célula na linha {row + 1} e coluna {col + 1}: ", 0, 9)
            if not (0 <= num <= 9):
                print("Número inválido. Tente novamente.")
                continue

            if self.is_valid(board, row, col, num):
                board[row][col] = num
                print("Número inserido com sucesso!")
            else:
                print("Número inválido. Tente novamente.")

            print("Tabuleiro atual:")
            self.print_board(board)

        return True

    def is_valid(self, board, row, col, num):
        for x in range(self.N):
            if board[row][x] == num or board[x][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False

        return True

    def is_solved(self, board):
        for i in range(self.N):
            for j in range(self.N):
                if board[i][j] == self.EMPTY:
                    return False
        return True

    def print_board(self, board):
        for row in range(self.N):
            for col in range(self.N):
                print(board[row][col], end=" ")
            print()

    def generate_random_sudoku(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.fill_diagonals(board)
        self.fill_remaining(board, 0, 3)
        self.make_some_cells_empty(board)
        return board

    def fill_diagonals(self, board):
        for i in range(0, self.N, 3):
            self.fill_box(board, i, i)

    def is_safe(self, board, row, col, num):
        for x in range(self.N):
            if board[row][x] == num or board[x][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False

        return True

    def fill_box(self, board, row, col):
        for i in range(3):
            for j in range(3):
                num = random.randint(1, 9)
                while not self.is_safe(board, row + i, col + j, num):
                    num = random.randint(1, 9)
                board[row + i][col + j] = num

    def fill_remaining(self, board, i, j):
        if j >= self.N and i < self.N - 1:
            i += 1
            j = 0
        if i >= self.N and j >= self.N:
            return True
        if i < 3:
            if j < 3:
                j = 3
        elif i < self.N - 3:
            if j == (i // 3) * 3:
                j += 3
        else:
            if j == self.N - 3:
                i += 1
                j = 0
                if i >= self.N:
                    return True
        for num in range(1, self.N + 1):
            if self.is_safe(board, i, j, num):
                board[i][j] = num
                if self.fill_remaining(board, i, j + 1):
                    return True
                board[i][j] = self.EMPTY
        return False

    def make_some_cells_empty(self, board):
        num_empty_cells = 40
        count = 0
        while count < num_empty_cells:
            row = random.randint(0, self.N - 1)
            col = random.randint(0, self.N - 1)
            if board[row][col] != self.EMPTY:
                board[row][col] = self.EMPTY
                count += 1

class Scanner:
    def input_int(self, message, min_val=None, max_val=None):
        while True:
            try:
                value = int(input(message))
                if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                    return value
                print(f"Por favor, digite um número entre {min_val} e {max_val}.")
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.main()
