import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def parse_poker_hand_puzzle_1(hand):
    # Count of how many occurences of each card
    card_count = {}
    for card in hand:
        if card not in card_count:
            card_count[card] = 1
        card_count[card] *= 3
        
    score = 0
    for key in card_count:
        if card_count[key] > 1:
            score += card_count[key] * 1000
    
    # now add the value of each card to the score
    for index, card in enumerate(hand):
        # make pos_score exponentially smaller based on the index
        pos_score = 20 / (20 ** index)
        score += pos_score * card

    return score

def parse_line_puzzle_1(line):
    hand, bid = line.split(" ")
    # convert hand to int by making sure we replace T, J, Q, K, A with 10, 11, 12, 13, 14
    hand = [int(card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")) for card in hand]
    return hand, int(bid)

def puzzle_1(lines):
    hands_with_score = []
    for line in lines:
        hand, bid = parse_line_puzzle_1(line)
        score = parse_poker_hand_puzzle_1(hand)
        hands_with_score.append({
            "line": line,
            "bid": bid,
            "score": score
        })
    
    # Sort the hands by score
    hands_with_score.sort(key=lambda x: x['score'], reverse=False)
    
    # Multiply each score by assigning a rank incrementally
    res = 0
    for rank, hand in enumerate(hands_with_score):
        x = hand['bid'] * (1+rank)
        res += x

    return res

def parse_poker_hand_puzzle_2(hand, hand_without_jocker):
    # Count of how many occurences of each card
    card_count = {}
    for card in hand_without_jocker:
        if card not in card_count:
            card_count[card] = 1
        card_count[card] *= 3
        
    score = 0
    for key in card_count:
        if card_count[key] > 1:
            score += card_count[key] * 1000
    
    # now add the value of each card to the score
    for index, card in enumerate(hand):
        # make pos_score exponentially smaller based on the index
        pos_score = 20 / (20 ** index)
        score += pos_score * card

    return score


def parse_line_puzzle_2(line):
    hand, bid = line.split(" ")
    # convert hand to int by making sure we replace T, J, Q, K, A with 10, 11, 12, 13, 14
    hand = [int(card.replace("T", "10").replace("J", "1").replace("Q", "12").replace("K", "13").replace("A", "14")) for card in hand]
    return hand, int(bid)

# QJJQ2 -> QQQQ2
def replace_jocker(hand):
    hand = hand.copy()

    # Count of how many occurences of each card
    card_count = {}
    for card in hand:
        if card == 1:
            continue
        if card not in card_count:
            card_count[card] = 1
        card_count[card] += 1

    # Sort card_count by value, otherwise by key
    sorted_cards_keys = sorted(card_count.items(), key=lambda x: (x[1], x[0]), reverse=True)

    if len(sorted_cards_keys) == 0:
        return [14,14,14,14,14]

    # Replace the first X with the best possible value
    for index, card in enumerate(hand):
        if card == 1:
            hand[index] = sorted_cards_keys[0][0]

    return hand



def puzzle_2(lines):
    hands_with_score = []
    for line in lines:
        hand, bid = parse_line_puzzle_2(line)
        # Fix hand by replacing "1" (the jocker) with best possible value
        hand_without_jocker = replace_jocker(hand)
        score = parse_poker_hand_puzzle_2(hand, hand_without_jocker)
        hands_with_score.append({
            "line": line,
            "bid": bid,
            "score": score
        })
    
    # Sort the hands by score
    hands_with_score.sort(key=lambda x: x['score'], reverse=False)
    
    # Multiply each score by assigning a rank incrementally
    res = 0
    for rank, hand in enumerate(hands_with_score):
        x = hand['bid'] * (1+rank)
        res += x

    return res


if __name__ == "__main__":
    with open(dir_path + "/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print("Puzzle 1:", puzzle_1(lines))
    print("Puzzle 2:", puzzle_2(lines))
