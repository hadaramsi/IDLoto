import random


def loto(hadar, sharon, yarden, chen, startSegment, endSegment):
    """
    :param hadar: Hadar Amsalem's ID
    :param sharon: Sharon Vazana's ID
    :param yarden: Yarden Hovav's ID
    :param chen: Chen Ben Tolila's ID
    :param startSegment: start Segment of range
    :param endSegment:  end Segment of range
    :return: the random choice of question
    """
    rnd = random.randint(0, 8)
    sum1 = hadar[rnd] + sharon[rnd] + yarden[rnd] + chen[rnd]
    if sum1 not in range(startSegment, endSegment + 1):
        sum1 = sum1 % (endSegment - startSegment + 1)
        sum1 += startSegment
    return sum1


def driver():
    """
    the main program
    :return: print results
    """
    hadar = [3, 1, 6, 1, 2, 9, 2, 1, 2]
    sharon = [2, 0, 6, 5, 1, 4, 0, 1, 0]
    yarden = [3, 1, 8, 2, 3, 0, 6, 5, 3]
    chen = [2, 0, 7, 2, 7, 8, 0, 2, 9]
    print("choice for part 1")
    print(loto(hadar, sharon, yarden, chen, 1, 9))
    print("choice for part 2")
    print(loto(hadar, sharon, yarden, chen, 10, 18))
    print(loto(hadar, sharon, yarden, chen, 10, 18))
    print("choice for part 3")
    print(loto(hadar, sharon, yarden, chen, 19, 30))
    print(loto(hadar, sharon, yarden, chen, 19, 30))
    print("choice for part 4")
    print(loto(hadar, sharon, yarden, chen, 31, 36))


driver()
