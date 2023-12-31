import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox(
                            (0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains.keys():
            domain_var = self.domains[var].copy()
            for word in domain_var:
                length = var.length
                if len(word) != length:
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        # function Revise(csp, X, Y):

        # revised = false
        # for x in X.domain:
        # if no y in Y.domain satisfies constraint for (X,Y):
        # delete x from X.domain
        # revised = true
        # return revised

        revised = False

        if x != y:
            overlap = self.crossword.overlaps[x, y]

        else:
            return revised

        if overlap == None:
            return revised

        print(overlap)

        domain_x = self.domains[x].copy()

        for word_x in domain_x:
            print(f"WORD_X: {word_x}")
            satisfied = False
            for word_y in self.domains[y]:
                if word_x[overlap[0]] == word_y[overlap[1]]:
                    satisfied = True
            if not satisfied:
                self.domains[x].remove(word_x)
                revised = True

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # function AC-3(csp):

        # queue = all arcs in csp
        # while queue non-empty:
        # (X, Y) = Dequeue(queue)
        # if Revise(csp, X, Y):
        # if size of X.domain == 0:
        # return false
        # for each Z in X.neighbors - {Y}:
        # Enqueue(queue, (Z,X))
        # return true

        if arcs == None:
            queue_pair = list(self.crossword.overlaps.keys())
        else:
            queue_pair = arcs
        while queue_pair:
            if len((queue_pair.pop(0),)) != 2:
                continue
            (x, y) = queue_pair.pop(0)
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x) - {y}:
                    queue_pair.append(z)

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.crossword.variables:
            if var in assignment.keys():
                continue
            else:
                return False

        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        words = list(assignment.values())
        print(f"words: {words}")

        # inconsistent if duplicate words
        if len(words) != len(set(words)):
            return False
        for var, word in assignment.items():
            # empty assignment
            if word == None:
                continue
            # inconsistent if violate variable length
            if var.length != len(word):
                return False
            neighbors = self.crossword.neighbors(var)

            print(f"neighbors: {neighbors}")

            for neighbor in neighbors:
                if neighbor not in assignment.keys():
                    continue
                overlap = self.crossword.overlaps[var, neighbor]
                # inconsistent if overlapping characters are not the same
                if word[overlap[0]] != assignment[neighbor][overlap[1]]:
                    return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        assignment_temp = assignment.copy()

        value_n_dict = {}

        for word in self.domains[var]:
            assignment_temp[var] = word

            neighbors = self.crossword.neighbors(var)

            n = 0
            for neighbor in neighbors:

                # neighbor that already got assigned is ignored
                if neighbor in assignment:
                    continue

                overlap = self.crossword.overlaps[var, neighbor]

                neighbor_domain = self.domains[neighbor]

                # if the word of neighbor domain is different from the overlapping, increase n
                for neighbor_word in neighbor_domain:
                    if neighbor_word[overlap[1]] != word[overlap[0]]:
                        n += 1

            value_n_dict[word] = n

        value_n_dict = {value: n for value, n in sorted(
            value_n_dict.items(), key=lambda x: x[1])}

        return value_n_dict.keys()

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        candidates = {}
        for var in self.crossword.variables:
            if var not in assignment.keys():
                candidates[var] = (len(self.domains[var]),
                                   len(self.crossword.neighbors(var)))

        candidates = sorted(candidates.items(),
                            key=lambda x: (x[1][0], 1 / x[1][1]))

        return candidates[0][0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        domain_var = self.order_domain_values(var, assignment)
        for value in domain_var:
            assignment_temp = assignment.copy()
            assignment_temp[var] = value
            if self.consistent(assignment_temp):
                assignment[var] = value
                result = self.backtrack(assignment)

                if result != None:
                    return result

                assignment.pop(var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
