def life(creature="MAN", year=0):

    if year == 0:
        year += 1
        print("At year " + str(year) + " He was Genius")
        return life(year=year+1)
    elif year ==  100:
        return print("At year " + str(year) + " He is dead")

    else:
        print("At year " + str(year)+ " parents, teachers , society makes him  dumb")
        return life(year=year+1)
life()