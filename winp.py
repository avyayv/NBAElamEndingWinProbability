from numpy.random import choice
import argparse

parser = argparse.ArgumentParser(description='Win Probabilities in OT')
parser.add_argument("scoreX", help="Score for the team with possession", type=int)
parser.add_argument("scoreY", help="Score for the team without possession", type=int)
args = parser.parse_args()

p0 = 0.505
p1 = 0.031
p2 = 0.325
p3 = 0.137
p4 = 0.002
average_pdist = [p0,p1,p2,p3,p4]

def sim(nsimulations, pdistx=average_pdist, pdisty=average_pdist, x_start=0, y_start=0, target_score=11):
    xwins = 0
    ywins = 0
    for games in range(0,nsimulations):
        xball = True
        x_score = x_start
        y_score = y_start
        while x_score < target_score and y_score < target_score:
            if xball:
                draw = choice([0,1,2,3,4], 1,
                      p=pdistx)
                x_score += draw
                xball = False
            else:
                draw = choice([0,1,2,3,4], 1,
                      p=pdisty)
                y_score += draw
                xball = True
            if x_score >= target_score:
                xwins += 1
            if y_score >= target_score:
                ywins += 1
    
    return xwins/(xwins+ywins)

simmed_value = sim(100000, x_start=args.scoreX, y_start=args.scoreY)
print("Probability of team with possession winning is", simmed_value)
print("Probability of team without possession winning is", 1-simmed_value)
