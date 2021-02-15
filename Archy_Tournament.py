import json

def Teams():
    with open ("Archy_Tournament.json") as f:
        participantList = json.load(f)
    return participantList

players = Teams()


def ShowParticipants(players):
    for i, j in players.items():
        print(i, "----->", j)

print('\n')
ShowParticipants(players)
print('\n')

def getScore(i,j, player,totalScore):
    A, B, C, D, E, F = 5, 4, 3, 2, 1, 0
    score = input("Enter the score for participant "+ player[j] + " in A, B, C, D, E, F :- ")
    if score == "A":
        totalScore = A+i
        return totalScore
    elif score == "B":
        totalScore = B+i
        return totalScore
    elif score == "C":
        totalScore = C+i
        return totalScore
    elif score == "D":
        totalScore = D+i
        return totalScore
    elif score == "E":
        totalScore = E+i
        return totalScore
    elif score == "F":
        totalScore = F
        return totalScore

def Rounds_of_the_game(players):

    Bonus_Team1 = 0
    Bonus_Team2 = 0
    Player1 = 0
    Player2 = 0 
    Player3 = 0
    Player4 = 0
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    
    for i in range(5):
        Team1 = 0
        Team2 = 0
        print("Round ", i+1)
        for team, player in players.items():
            for j in range(len(player)):
                if team == 'team1':
                    if player[j] == 'player1':
                        getscore = getScore(i,j,player,0)
                        score1 = getscore
                        Player1 = Player1 + getscore
                    elif player[j] == 'player2':
                        getscore = getScore(i,j,player,0)
                        score2 = getscore
                        Player2 = Player2 + getscore
                    if score1 == score2:
                        Bonus_Team1 = Bonus_Team1 + 2                       
                if team == 'team2':
                    if player[j] == 'player3':
                        getscore = getScore(i,j,player,0)
                        score3 = getscore
                        Player3 = Player3 + getscore
                    elif player[j] == 'player4':
                        getscore = getScore(i,j,player,0)
                        score4 = getscore
                        Player4 = Player4 + getscore
                    if score3 == score4:
                        Bonus_Team2 = Bonus_Team2 + 2

        print('Score of Player1 ',Player1)
        print('Score of Player2 ',Player2)
        print('Score of Player3 ',Player3)
        print('Score of Player4 ',Player4)
        print('\n')

        print('Bonus of Team1 ',Bonus_Team1)
        print('Bonus of Team2 ',Bonus_Team2)
        print('\n')
        
        Team1 = Team1 + Player1 + Player2 + Bonus_Team1
        print('Total Score of Team1 ', Team1)
        Team2 = Team2 + Player3 + Player4 + Bonus_Team2
        print('Total Score of Team2 ', Team2)
        print('\n')

        if Team1 == Team2 >= 60:
            print("Drow")
        elif Team1 >= 60 and Team2 >= 60:
            if Team1 > Team2:
                print("Team1 won the match")
            else:
                print("Team2 won the match")
            break
        elif Team1 >= 60:
            print("Team1 won the match")
            break
        elif Team2 >= 60:
            print("Team2 won the match")
            break

Rounds_of_the_game(players)


