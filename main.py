import copy

class TwentyQuestions:
    def __init__(self):
        self._root = None

    def guess_routine(self):
        count = 0
        current_node = self._root

        print()
        print('***Let\'s play! ***')
        print()
        print('Think of a creature...')

        if not current_node:
            creature = input("There are no creatures loaded, please tell me your creature. ")
            print("Thank you! Now we can play")
            self._root = BinaryTreeNode(creature)
            return

        if current_node and not current_node.left_child and not current_node.right_child:
            self._input_getter(current_node)

        while current_node.left_child or current_node.right_child and count <= 20:
            current_node = self._pseudo_recurser(current_node)

    # def _pseudo_recurser(self, current_node):
    #     print()
    #     print('***Let\'s play! ***')
    #     print()
    #     print('Think of a creature...')
    #     answer = input(current_node.data)
    #     if answer.upper() == 'Y':
    #         current_node = current_node.left_child
    #     elif answer.upper() == 'N':
    #         current_node = current_node.right_child
    #     else:
    #         print("Incorrect answer, starting over")
    #         return current_node

    def _input_getter(self, current_node):
        if current_node == self._root:
            answer = input(f"Is this your creature: {current_node.data} (Y/N): ")
            if answer.upper() == 'Y':
                print('Excellent, thank you for playing!')
                return
        else:
            print(current_node.data)
            answer = input("Please enter Y or N ")

        if answer.upper() == 'N':
            new_animal = input("What is your creature? ")
            new_question = input(f"Please enter a yes or no question "
                                 f"that will distinguish "
                                 f"{current_node.data} from "
                                 f"{new_animal}. ")
            tree_decider = input(f"For your creature {new_animal}, "
                                 f"{new_question}? (Y/N) ")

            self._node_maker(current_node, new_animal, new_question, tree_decider)
            # if tree_decider.upper() == 'Y':
            #     self._node_maker(current_node,new_animal, new_question,
            #                      current_node.left_child,
            #                      current_node.right_child)
            # elif tree_decider.upper() == 'N':
            #     self._node_maker(current_node,new_animal, new_question,
            #                      current_node.right_child,
            #                      current_node.left_child)

    def _node_maker(self, current_node, new_animal, new_question,
                    tree_decider):
        new_node = copy.deepcopy(current_node)

        if tree_decider.upper() == 'Y':
            current_node.right_child = new_node
            current_node.left_child = BinaryTreeNode(new_animal)
            current_node.data = new_question

        elif tree_decider.upper() == 'N':
            current_node.left_child = new_node
            current_node.right_child = BinaryTreeNode(new_animal)
            current_node.data = new_question
        print(f"Thank you, I have added {new_animal} to the database")
        return




# tree with the following properties:

# Every node that is not a leaf node will have a left and a right child
# A node that is not a leaf node will contain a yes or no question as data.
        # Animals that fit a "Yes" answer will be in the left subtree, and
        # animals that fit a "No" answer will be in the right subtree.
# Leaf nodes contain an animal as data
# In the class we only need two methods:
#
# def __init__()
# The constructor will create a single attribute that will represent the root
        # of the tree.  Initially we set this to None.
#
# def guess_routine()
# This method will traverse the tree, asking questions to narrow down the guess.
# A "yes" answer from the use traverses to the left, and a "no" answer
# traverses to the right.  The computer makes a guess when it hits a
# leaf node.
#
# If the computer guesses correctly, exit the method without making any changes
        # to the tree.
#
# If the computer guesses incorrectly, as the user for a yes or no question
# that will distinguish the computer's guess from the correct animal.  Ask the
# user whether the answer would be "yes" or "no" for their animal.
# Set the current node's data to the question string, and create a left
# and right node containing the two animal names.  You will need some
# logic to determine which one goes on the left, and which one goes on
# the right.
#
# Add some module level code to create an object of the TwentyQuestions class.  Call guess_routine() in a loop.

class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


if __name__ == '__main__':
    guessing_game = TwentyQuestions()
    while True:
        guessing_game.guess_routine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
