score_system = {
        'Rock vs. Losing move' : 3,
        'Rock vs. Drawing move' : 4,
        'Rock vs. Winning move' : 8,
        'Paper vs. Losing move' : 1,
        'Paper vs. Drawing move' : 5,
        'Paper vs. Winning move' : 9,
        'Scissors vs. Losing move' : 2,
        'Scissors vs. Drawing move' : 6,
        'Scissors vs. Winning move' : 7
    }

with open("input.txt", 'r') as file:
    rounds = file.read()
    rounds = rounds.replace('A', "Rock vs.").replace('B', "Paper vs.").replace('C', "Scissors vs.")
    rounds = rounds.replace('X', "Losing move").replace('Y', "Drawing move").replace('Z', "Winning move")
    rounds = rounds.split('\n')

    score = 0
    for round in rounds:
        score += score_system.get(round)
        
    print(score)