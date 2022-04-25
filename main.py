
class TwentyQuestions:
    """Play the 20 questions game

        Args:
            None
        Returns:
            None
    """
    def __init__(self):
        self._root = None

    # guessing game funtion
    def guess_routine(self):
        steps = 0
        while steps <= 20:
            print()
            print('***Let\'s play! ***')
            print()
            print('Think of a creature...')

            #check if the tree is empty, and if so, create first now
            if self._root is None:
                creature = input("There are no creatures loaded, please tell me your creature. ")
                print("Thank you! Now we can play.")
                self._root = BinaryTreeNode(creature)

            #if tree != empty, traverse tree, asking questions
            else:
                current_node = self._root
                while current_node.left_child:
                    print(current_node.data)
                    answer = input("Please enter Y or N ")
                    if answer.upper() == 'Y':
                        current_node = current_node.left_child
                    elif answer.upper() == 'N':
                        current_node = current_node.right_child
                    else:
                        print("Incorrect answer, starting over")
                        return current_node

                #guess if the node your traversal leads to is the creature
                answer = input(f"Is this your creature: {current_node.data} (Y/N): ")

                #if that is creature, print congrats and exit loop
                if answer.upper() == 'Y':
                    print('Excellent, thank you for playing!')

                #if not, gather new question, new animal, store reorder nodes
                else:
                    # what kind of animal? (store in new_animal node)
                    new_animal = input("What is your creature? ")
                    new_animal_node = BinaryTreeNode(new_animal)

                    # new node for current_node's animal (call it old_animal)
                    old_animal_node = BinaryTreeNode(current_node.data)

                    #ask for differentiating questinos between new_animal and current_node
                    new_question = input(f"Please enter a yes or no question "
                                         f"that will distinguish "
                                         f"{current_node.data} from "
                                         f"{new_animal}. ")
                    #place the question in to the current node
                    current_node.data = new_question
                    #ask the user whether the answer is yes or no for their new animal
                    tree_decider = input(f"For your creature {new_animal}, "
                                         f"{new_question} (Y/N) ")

                    #order the leaf nodes according to the users response
                    if tree_decider.upper() == 'Y':
                        current_node.left_child = new_animal_node
                        current_node.right_child = old_animal_node
                    else:
                        current_node.left_child = old_animal_node
                        current_node.right_child = new_animal_node
                    print(f"Thank you, I have added {new_animal} to the database")


class BinaryTreeNode:
    """Template class for node in a binary tree

        Args:
            data (any type): data to be stored in the node
        Returns:
            None
    """
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


if __name__ == '__main__':

    guessing_game = TwentyQuestions()
    #initiate guessing game routine
    while True:
        guessing_game.guess_routine()

##Sample Run
# /Users/isaacmather/PycharmProjects/Assignment3/venv/bin/python /Users/isaacmather/PycharmProjects/Assignment3/main.py
#
# ***Let's play! ***
#
# Think of a creature...
# There are no creatures loaded, please tell me your creature. Cat
# Thank you! Now we can play
#
# ***Let's play! ***
#
# Think of a creature...
# Is this your creature: Cat (Y/N): N
# What is your creature? Dog
# Please enter a yes or no question that will distinguish Cat from Dog. Does it bark?
# For your creature Dog, Does it bark?? (Y/N) Y
# Thank you, I have added Dog to the database
#
# ***Let's play! ***
#
# Think of a creature...
# Does it bark?
# Please enter Y or NN
# Is this your creature: Cat (Y/N): N
# What is your creature? Giraffe
# Please enter a yes or no question that will distinguish Cat from Giraffe. Does it have long legs?
# For your creature Giraffe, Does it have long legs?? (Y/N) Y
# Thank you, I have added Giraffe to the database
#
# ***Let's play! ***
#
# Think of a creature...
# Does it bark?
# Please enter Y or Nn
# Does it have long legs?
# Please enter Y or Ny
# Is this your creature: Giraffe (Y/N): n
# What is your creature? Spider
# Please enter a yes or no question that will distinguish Giraffe from Spider. Does it have a long neck?
# For your creature Spider, Does it have a long neck?? (Y/N) n
# Thank you, I have added Spider to the database
#
# ***Let's play! ***
#
# Think of a creature...
# Does it bark?
# Please enter Y or Nn
# Does it have long legs?
# Please enter Y or Ny
# Does it have a long neck?
# Please enter Y or Ny
# Is this your creature: Giraffe (Y/N): y
# Excellent, thank you for playing!
#
# ***Let's play! ***
#
# Think of a creature...
# Does it bark?
# Please enter Y or N