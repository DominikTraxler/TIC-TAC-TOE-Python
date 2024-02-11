import random
from termcolor import colored

class Board:
    def __init__(self, state, CurrentPlayer):
        self.state = state
        self.Endstate = self.EndStateChecking(self.state)
        self.PMoves = self.GetMoves(self.state)
        self.CurrentPlayer = CurrentPlayer
        #print("Stats of Class: ", self.state, self.Endstate, self.PMoves, CurrentPlayer)
    
    def GetMoves(self, Board):
        listOfMoves = []
        i=0
        while(i < 9):
            if(Board[i] == ""):
                listOfMoves.append(i)
            i += 1
        return listOfMoves

    def EndStateChecking(self, TheBoard):
        #Horizontal check
        ThreeCount = ""
        i=0
        while(i < 3):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 1
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)
        ThreeCount = ""
        while(i < 6):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 1
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)
        ThreeCount = ""
        while(i < 9):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 1
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)

        #VerticalCheck
        i=0
        ThreeCount = ""
        while(i < 9):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 3
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)
        i=1
        ThreeCount = ""
        while(i < 10):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 3
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)
        i=2
        ThreeCount = ""
        while(i < 10):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 3
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)
        #Diagonal Check
        i=0
        ThreeCount = ""
        while(i<10):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 4
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)
        i=2
        ThreeCount = ""
        while(i<8):
            if(TheBoard[i] == "O"):
                ThreeCount = f"{ThreeCount}O"
            elif(TheBoard[i] == "X"):
                ThreeCount = f"{ThreeCount}X"
            i += 2
            if(ThreeCount == "OOO"):
                return(1)
            if(ThreeCount == "XXX"):
                return(2)

        #Draw Check
        i=0
        NineCount = 0
        while(i < 9):
            if(TheBoard[i] != ""):
                NineCount += 1
            i += 1
        if(NineCount == 9):
            return(3)

        return(0)




def CheckIfEnd(TheBoard):
    #Vertikal check
    ThreeCount = ""
    i=0
    while(i < 3):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 1
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    ThreeCount = ""
    while(i < 6):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 1
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    ThreeCount = ""
    while(i < 9):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 1
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    
    #VerticalCheck
    i=0
    ThreeCount = ""
    while(i < 9):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 3
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    i=1
    ThreeCount = ""
    while(i < 10):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 3
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    i=2
    ThreeCount = ""
    while(i < 10):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 3
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    #Diagonal Check
    i=0
    ThreeCount = ""
    while(i<10):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 4
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    i=2
    ThreeCount = ""
    while(i<8):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 2
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)

    #Draw Check
    i=0
    NineCount = 0
    while(i < 9):
        if(TheBoard[i] != ""):
            NineCount += 1
        i += 1
    if(NineCount == 9):
        return(3)
    
    return(0)

def GetMoves(Board):
    listOfMoves = []
    i=0
    while(i < 9):
        if(Board[i] == ""):
            listOfMoves.append(i)
        i += 1
    return listOfMoves, len(listOfMoves)

def AIMoveRandom(TheBoard):
    #Board1 = Board(TheBoard)
    PossibleMoves, AmountOfMoves = GetMoves(TheBoard)
    RandomMove = random.randint(0, AmountOfMoves-1)
    """
    print("Amount of Moves: " + str(AmountOfMoves))
    print("PossibleMoves: " + str(PossibleMoves))
    print("ChosenMove: " + str(PossibleMoves[RandomMove]))
    """
    return PossibleMoves[RandomMove]

def AIMoveEndAvoidant(TheBoard, CurrentPlayer):
    MainBoard = Board(TheBoard, CurrentPlayer)
    #print(f"Current Player: {CurrentPlayer}")
    PMoves = list(MainBoard.PMoves)
    NextPlayer = 0

    Symbol = ""
    if(CurrentPlayer == 1):
        Symbol = "O"
        NextPlayer = 2
    if(CurrentPlayer == 2):
        Symbol = "X"
        NextPlayer = 1

    #Get all the next possible positions
    ListOfBoards = []
    NamesOfBoards = ["Board0", "Board1", "Board2", "Board3", "Board4", "Board5", "Board6", "Board7", "Board8"]
    i = 0
    while (i < len(PMoves)):
        RealMove = PMoves[i]
        newState = []
        newState = list(MainBoard.state)
        newState[RealMove] = Symbol
        NamesOfBoards[i] = Board(newState, NextPlayer)
        ListOfBoards.append(NamesOfBoards[i])
        i += 1

    #Evaluate each position
    ListOfBoardEvaluations = []
    i = 0
    while(i < len(ListOfBoards)):
        BoardInQuestion = ListOfBoards[i]
        if(BoardInQuestion.Endstate == 0):
            ListOfBoardEvaluations.append(0)
        elif(BoardInQuestion.Endstate == CurrentPlayer):
            ListOfBoardEvaluations.append(1)
            print(colored("-- Win identified --", "green"))
        elif(BoardInQuestion.Endstate == NextPlayer):
            ListOfBoardEvaluations.append(-1)
        elif(BoardInQuestion.Endstate == NextPlayer):
            ListOfBoardEvaluations.append(0)
        i += 1
    #print(f"List of Board Evalutaions: {ListOfBoardEvaluations}")
    
    #Deside which position move to play
    bestEval = max(ListOfBoardEvaluations)
    #print(f"BestEval: {bestEval}")
    ListOfMaxEval = []
    for value in ListOfBoardEvaluations:
        if (value == bestEval):
            ListOfMaxEval.append(1)
        elif(value < bestEval):
            ListOfMaxEval.append(0)
    #print(f"List of max eval: {ListOfMaxEval}")

    ListOfMaxEvalPositions = []
    i = 0
    while(i < len(ListOfMaxEval)):
        if(ListOfMaxEval[i] == 1):
            ListOfMaxEvalPositions.append(PMoves[i])
        i += 1
    #print(f"ListOfMaxEvalPositions: {ListOfMaxEvalPositions}")

    if(len(ListOfMaxEvalPositions) != 1):
        lenghtOfList = len(ListOfMaxEvalPositions)
        #print(f"Length of list:  {lenghtOfList}")
        randomNum = random.randint(0, lenghtOfList - 1)
        #print(f"Random Number between 0 and {len(ListOfMaxEvalPositions) - 1}: {randomNum}")
        finalMove = ListOfMaxEvalPositions[randomNum]
    elif(len(ListOfMaxEvalPositions) == 1):
        finalMove = ListOfMaxEvalPositions[0]
    #print(f"Final Move: {finalMove}")
    return finalMove