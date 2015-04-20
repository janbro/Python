# The function localize takes the following arguments:
#
# colors:       a 2D list, each entry either 'R' (for a red cell) or 'G' (for a green cell)
#
# measurements: a list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:      a list of actions taken by the robot, each entry of the form [dy,dx], where
#               dx refers to the change in the x-direction (positive meaning movement to the right)
#               and dy refers to the change in the y-direction (positive meaning movement downward)
#               NOTE: the *first* coordinate is change in y; the *second* coordinate is change in x
#
# sensor_right: a float between 0 and 1, giving the probability that any given measurement is
#               correct; the probability that the measurement is incorrect is 1-sensor_right
#
# p_move:       a float between 0 and 1, giving the probability that any given movement command takes
#               place; the probability that the movement command fails (and the robot remains still);
#               the robot will NOT overshoot its destination in this exercise
#
# The function should RETURN (not just show) a 2D list (of the same dimensions as colors) that 
# gives the probabilities that the robot occupies each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform probability of being 
# in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
    count = 0
    for sense in measurements:
        p = [[p[(row-motions[count][0])%len(colors)][(col-motions[count][1])%len(colors[0])]*p_move+p[row][col]*(1.0-p_move) for col in range(len(colors[0]))] for row in range(len(colors))]
        p = [[p[row][col]*sensor_right*(sense==colors[row][col])+p[row][col]*(1.0-sensor_right)*(sense!=colors[row][col]) for col in range(len(colors[0]))] for row in range(len(colors))]
        
        count+=1
        
    su = sum([sum(li) for li in p])
    p = [[p[row][col]/su for col in range(len(colors[0]))] for row in range(len(colors))]
    
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = .7
p_move = .8
p = localize(colors,measurements,motions,sensor_right,p_move)
show(p) # displays your answer
