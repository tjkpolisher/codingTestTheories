def solution(players, callings):
    positions = {player: i for i, player in enumerate(players)}
    for call in callings:
        i = positions[call]
        players[i-1], players[i] = players[i], players[i-1]
        positions[players[i-1]] = i-1
        positions[players[i]] = i
    return players