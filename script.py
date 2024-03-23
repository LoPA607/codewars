import random
import math

name = "script"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )
    
def checkIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False


def ActPirate(pirate):
    # complete this function
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        b += 1
        pirate.setSignal("left")

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        b += 1
        pirate.setSignal("left")

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        b += 1

        pirate.setSignal("left")


    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        b += 1
        pirate.setSignal("left")


    if (
        (up == "island1" and s[0] == "myCaptured")
        or (up == "island2" and s[1] == "myCaptured")
        or (up == "island3" and s[2] == "myCaptured") 
    ):
        pirate.setSignal("left")

    if (
        (right == "island1" and s[0] == "myCaptured")
        or (right == "island2" and s[1] == "myCaptured")
        or (right == "island3" and s[2] == "myCaptured") 
    ):
        # pirate.SetTeamSignal(s)
        pirate.setSignal("left")

    if (
        (down == "island1" and s[0] == "myCaptured")
        or (down == "island2" and s[1] == "myCaptured")
        or (down == "island3" and s[2] == "myCaptured") 
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setSignal("left")


    if (
            (left == "island1" and s[0] == "myCaptured")
            or (left == "island2" and s[1] == "myCaptured")
            or (left == "island3" and s[2] == "myCaptured") 
        ):
            pirate.setSignal("left")

    if (up == "friend"):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            s = up[-1] + str(x) + "," + str(y + 1)
            pirate.setSignal("move")
    
    if (down == "friend"):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            s = up[-1] + str(x) + "," + str(y - 1)
            pirate.setSignal("move")
    
    if (left == "friend"):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            s = up[-1] + str(x - 1) + "," + str(y)
            pirate.setSignal("move")
    
    if (right == "friend" ) :
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            s = up[-1] + str(x + 1) + "," + str(y)
            pirate.setSignal("move")

    if (up != "friend" and up != "enemy" ):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            pirate.setSignal("random")
    
    if (down != "friend" and down != "enemy"):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            pirate.setSignal("random")
    
    if (left != "friend" and left != "enemy" ):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            pirate.setSignal("random")
    
    if (right != "friend" and right != "enemy"):
        if checkIsland(pirate) and b<= 4:
            pirate.setSignal("left")
        else:
            pirate.setSignal("random")

    if pirate.getSignal() =="left":
        return 0

    elif pirate.getSignal() == "move":
        s = pirate.GetCurrentTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
        return moveTo(x, y, pirate)
    
    elif pirate.getSignal() == "random":
        return random.randint(1,4)

    pass


def ActTeam(team):
    if team.getTotalPirates()>150 & team.getTotalRum()>50 & team.getTotalGunpowder()>50:
    # complete this function
     l = team.trackPlayers()
     s = team.getTeamSignal()

     team.buildWalls(1)
     team.buildWalls(2)
     team.buildWalls(3)

     if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
     pass