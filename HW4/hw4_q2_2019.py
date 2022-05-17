"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2019
hw4_q2_sol_2019.py - DP planks with turtle
"""
import turtle


def dpChoosePlanks(plankList, totalDistance, minPlanks, planksUsed):
    """
     plankList = [1,5,10,21,25] # list of possible planks
     distance = 63 # Actual amount
     minPlanks = [0,0...0] (64)
     planksUsed = [0,0...0] (64)
    """
    count = 0 # initialize counting variable
    for dist in range(totalDistance + 1):  # loop 64 times
        plankCount = dist
        newPlank = 1
        for j in [c for c in plankList if c <= dist]: # checks each plank type to see if it works
            count += 1 # add one (used for dynamic iterations)
            if minPlanks[dist-j] + 1 < plankCount: # if selected plank is shorter than plank count...
                plankCount = minPlanks[dist-j]+1
                newPlank=j
            minPlanks[dist] = plankCount
            planksUsed[dist] = newPlank
    print("dynamic_p number of iterations:{}".format(count))
    return minPlanks[totalDistance]


def printPlanks(planksUsed, totalDistance):
    dist = totalDistance
    plankOrder=[]
    while dist > 0:
        thisDistance = planksUsed[dist]
        plankOrder.append(thisDistance)
        print("In printPlanks:plank:{}".format(thisDistance))
        dist = dist - thisDistance
    print(plankOrder[::-1])
    return plankOrder[::-1]


def side(steps,t,color):
    for step in steps:
        t.color(color[step])
        t.forward(step)

def plankSetup(totalDist, plankList):
    planksUsed = [0] * (totalDist + 1)
    distCovered = [0] * (totalDist + 1)
    print("Making distance for", totalDist, "requires")
    print(dpChoosePlanks(plankList, totalDist, distCovered, planksUsed), "planks")
    print("They are:")
    A_list = printPlanks(planksUsed, totalDist)
    return A_list

if __name__ == '__main__':
    def main():

        t = turtle.Turtle()
        myWin = turtle.Screen()
        t.shape("classic")
        t.speed(1)

        a_Dist = int(input("Enter value for 'a': "))
        b_Dist = int(input("Enter value for 'b': "))
        plankList = [1, 5, 10, 21, 25]
        plankColor = {1:'red',5:'blue',10:'black',21:'green',25:'violet'}

        A_list=plankSetup(a_Dist,plankList)

        t.left(90)
        print("A_list:{}".format(A_list))
        side(A_list,t,plankColor)

        t.right(90)
        B_list = plankSetup(b_Dist, plankList)
        print("B_list:{}".format(B_list))
        side(B_list, t, plankColor)

        t.right(90)
        print("A_list:{}".format(A_list))
        side(A_list, t, plankColor)

        t.right(90)
        print("B_list:{}".format(B_list))
        side(B_list, t, plankColor)

        myWin.exitonclick()

if __name__ == '__main__':
    main()