from PyQt6.QtWidgets import *
from gui_VotingMenu import *
from gui_VoteTally import *
from gui_CandidateMenu import *


john_votes:int = 0
jane_votes:int = 0


class Window1(QMainWindow, Ui_MainWindow1_VoteMenu):
    """
    The starter window (aka the "Vote Menu").
    Contains the "Vote" and "Exit" button.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.VoteButton.clicked.connect(lambda  : self.vote())
        self.ExitButton.clicked.connect(lambda : self.exit())

    def vote(self):
        """
        Executes when "Vote" button is clicked.
        Takes user to "Candidate Menu" window (Window2).
        """
        window2 = Window2()
        window2.show()
        self.close()

    def exit(self):
        """
        Executes when "Exit" button is clicked.
        Closes the "Vote Menu" (Window1), and opens the "Tally" window.
        """
        self.close()

        window3 = Window3()
        window3.show()


class Window2(QMainWindow, Ui_MainWindow2_CandidateMenu):
    """
    The "Candidate Menu" window.
    Contains the "John" and "Jane" buttons (the candidate buttons).
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.JohnButton.clicked.connect(lambda: self.add_john())
        self.JaneButton.clicked.connect(lambda: self.add_jane())


    def add_john(self):
        """
        Executes when user clicks the "John" button.
        Increments the variable "john_votes" (adds one vote to John's tally),
        then closes the "Candidate Menu" window (Window2).
        """
        global john_votes
        john_votes += 1

        self.open_vote_menu()
        self.close()

    def add_jane(self):
        """
        Executes when user clicks the "Jane" button.
        Increments the variable "jane_votes" (adds one vote to Jane's tally),
        then closes the "Candidate Menu" window (Window2).
        """
        global jane_votes
        jane_votes += 1

        self.open_vote_menu()
        self.close()

    def open_vote_menu(self):
        """
        Reopens the "Vote Menu" window.
        :return:
        """
        vote_menu = Window1()
        vote_menu.show()


class Window3(QMainWindow, Ui_MainWindow3_VoteTally):
    """
    The "Tally" window.
    Contains an "Exit" button and labels that display the tally
    for each candidate as well as the total number of votes.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.change_totals()
        self.ExitButton2.clicked.connect(lambda: self.exit_tally())

    def exit_tally(self):
        """
        Executes when "Exit" button is clicked.
        Closes the window.
        """
        self.close()

    def change_totals(self):
        """
        Executes on Window3 initiation.
        Changes the tally labels to their corresponding values.
        """
        self.JohnCount_label.setText(str(john_votes))
        self.JaneCount_label.setText(str(jane_votes))
        self.TotalCount_label.setText(str(john_votes + jane_votes))
