import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        count = cell
        """
        if len(self.cells) == self.count:
            return self.cells

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        count = 0
        """

        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:

        """
        # 1) mark the cell as a move that has been made
        self.moves_made.add(cell)

        # 2) mark the cell as safe
        self.mark_safe(cell)

        # 3) add a new sentence to the AI's knowledge base
        #      based on the value of `cell` and `count`

        # identifying neighbors that are not in safes or mines
        neighbors = set()
        modified_count = copy.deepcopy(count)
        for x, y in [(cell[0]+a, cell[1]+b) for a in (-1, 0, 1) for b in (-1, 0, 1)]:
            if not (0 <= x < self.height and 0 <= y < self.width) or (x, y) == cell:
                continue
            if (x, y) in self.mines:
                modified_count -= 1
                continue
            if (x, y) not in self.safes:
                neighbors.add((x, y))

        new_sentence = Sentence(neighbors, modified_count)

        if len(new_sentence.cells) > 0:
            self.knowledge.append(new_sentence)

        # 4) mark any additional cells as safe or as mines
        # if it can be concluded based on the AI's
        # knowledge base

        self.update_knowledge()

        # 5) add any new sentences to the AI's knowledge base
        #        if they can be inferred from existing knowledge
        # subset method
        # Check if one set is a subset of another

        for index, sentence_A in enumerate(self.knowledge):
            for sentence_B in self.knowledge[index+1:]:
                set_A = sentence_A.cells
                set_B = sentence_B.cells
                count_A = sentence_A.count
                count_B = sentence_B.count
                if set_A.issubset(set_B):
                    new_sentence = Sentence(set_B - set_A, count_B - count_A)
                    # self.knowledge.append(new_sentence)
                    more_mines = new_sentence.known_mines()
                    more_safes = new_sentence.known_safes()
                    if more_mines:
                        for m in more_mines:
                            self.mark_mine(m)
                    if more_safes:
                        for s in more_safes:
                            self.mark_safe(s)

    def update_knowledge(self):

        # 4) mark any additional cells as safe or as mines
        # if it can be concluded based on the AI's
        # knowledge base

        knowledge_cp = copy.deepcopy(self.knowledge)
        for sentence in knowledge_cp:
            # print(f"sentence: {sentence}")
            more_mines = sentence.known_mines()
            more_safes = sentence.known_safes()
            if more_mines:
                # print(f"more mines: {more_mines}")
                for m in more_mines:
                    self.mark_mine(m)
                    self.update_knowledge()
            if more_safes:
                # print(f"more safes: {more_safes}")
                for s in more_safes:
                    self.mark_safe(s)
                    self.update_knowledge()

        # remove empty knowledge
        self.knowledge[:] = [
            cell for cell in self.knowledge if cell != Sentence(set(), 0)]

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        safe_moves = []
        for cell in self.safes:
            if cell not in self.moves_made:
                safe_moves.append(cell)
        if safe_moves:
            return random.choice(safe_moves)
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        grid_cells = []
        available_moves = []

        for i in range(8):
            for j in range(8):
                grid_cells.append((i, j))

        for cell in grid_cells:
            if cell not in self.moves_made and cell not in self.mines:
                available_moves.append(cell)

        if available_moves:
            return random.choice(available_moves)
        else:
            return None
