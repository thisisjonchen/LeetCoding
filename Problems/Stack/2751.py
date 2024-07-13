# LC 2751. Robot Collisions | Daily - 7/13/24, O(nlogn)
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robotHp = dict()
        robotDir = dict()
        for i in range(len(positions)):
            robotHp[positions[i]] = healths[i]
            robotDir[positions[i]] = directions[i]
        collisionField = []
        surviving = []
        sortedPos = sorted(positions)

        for i in range(len(positions)):
            if robotDir[sortedPos[i]] == "R":
                collisionField.append(sortedPos[i])
            elif robotDir[sortedPos[i]] == "L":
                while robotHp[sortedPos[i]] > 0 and len(collisionField) != 0:
                    collidingRob = collisionField.pop()
                    if robotHp[collidingRob] > robotHp[sortedPos[i]]:
                        robotHp[collidingRob] = robotHp[collidingRob] - 1
                        collisionField.append(collidingRob)
                        robotHp[sortedPos[i]] = 0
                    elif robotHp[collidingRob] < robotHp[sortedPos[i]]:
                        robotHp[sortedPos[i]] = robotHp[sortedPos[i]] - 1
                        robotHp[collidingRob] = 0
                    else:
                        robotHp[sortedPos[i]] = 0
                        robotHp[collidingRob] = 0
                if len(collisionField) == 0 and robotHp[sortedPos[i]] > 0:
                    surviving.append(sortedPos[i])

        for robot in range(len(collisionField)):
            surviving.append(robot)
        res = []
        for robotPos in positions:
            if robotHp[robotPos] > 0:
                res.append(robotHp[robotPos])
        return res

'''
TLDR: Use dicts to keep track of health and dir using pos as key. Sort the positions to keep track, add "R" to collision field. Surviving "L" after all possible collisions in collisionField will always be surviving. 
At the end, empty out collisionField, reiterate through positions (has to return in that order), and return. O(nlogn) due to sorting.
'''

            



