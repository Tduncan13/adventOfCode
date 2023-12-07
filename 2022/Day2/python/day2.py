#!/usr/bin/python3

scores = [1, 2, 3]


def process_moves(move, origin):
    return ord(move) - ord(origin)


def part1(data):
    score = 0
    
    for line in data: 
        moves = line.strip('\n').split(' ')

        opponent_move = process_moves(moves[0], 'A')
        player_move = process_moves(moves[1], 'X')
        winning_move = (opponent_move + 1) % 3

        if player_move == winning_move:
             score = score + scores[player_move] + 6
        elif player_move == opponent_move :
            score = score + scores[player_move] + 3
        else:
            score = score + scores[player_move]
            
    return score
        

def part2(data):
    
    score = 0
    sg = {'X': 2, 'Y': 0, 'Z': 1}
    
    for line in data: 
        moves = line.strip('\n').split(' ')
        
        opponent_move = process_moves(moves[0], 'A')
        required_move = (opponent_move + sg[moves[1]]) % 3 
        
        if moves[1] == 'Z': 
            score = score + scores[required_move] + 6
        elif moves[1] == 'Y':
            score = score + scores[required_move] + 3
        else:
            score = score + scores[required_move]
            
    return score


if __name__ == "__main__":
    test = './test_input.txt'
    p1 = './input1.txt'
    p2 = './input2.txt'
    data = open(p1, 'r')
    print("--- Part 1 ---")
    print(part1(data.readlines()))
    data = open(p2, 'r')
    print("--- Part 2 ---")
    print(part2(data.readlines()))
