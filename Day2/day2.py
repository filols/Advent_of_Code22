score_system = {
        'Rock Rock' : 4,
        'Rock Paper' : 8,
        'Rock Scissors' : 3,
        'Paper Rock' : 1,
        'Paper Paper' : 5,
        'Paper Scissors' : 9,
        'Scissors Rock' : 7,
        'Scissors Paper' : 2,
        'Scissors Scissors' : 6
    }

with open("input.txt", 'r') as file:
    score = 0

    rounds = (file.read().replace('X', 'A').replace('Y', 'B').replace('Z', 'C').replace('A', "Rock")
                .replace('B', "Paper").replace('C', "Scissors").split('\n'))
    for round in rounds:
        score += score_system.get(round)
        
    print(score)