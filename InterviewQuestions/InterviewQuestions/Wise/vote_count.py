def voteCount(votes):
    """
    :param votes: list of names
    :return: new list of names with highest occurrence in alphabetical order
    """
    voteCounter = {}

    # Count the votes
    for vote in votes:
        if vote in voteCounter:
            voteCounter[vote] = voteCounter[vote] + 1
        else:
            voteCounter[vote] = 1

    # Find max votes
    maxCount = 0
    for vote, count in voteCounter.iteritems():
        if count > maxCount:
            maxCount = count

    # Find max winner
    winners = []
    for vote, count in voteCounter.iteritems():
        if count == maxCount:
            winners.append(vote)

    return sorted(winners)


if __name__ == '__main__':
    votes = ['Caleb', 'George', 'Ryan', 'Caleb', 'Phil', 'George', 'Ryan', 'Rob']

    print(voteCount(votes))
