##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

last_position = (0,0)
backward=0
visited_locations = [(0,0)]
last_move = None

##############################################################
# Please put your code here (imports, variables, functions...)
##############################################################

# Import of random module
import random




def random_feasable_location ( maze_map , source_location ) :
    
    global visited_locations
    global last_location
    not_visited=[]
    
    if source_location not in visited_locations :
      visited_locations.append(source_location)
    
    # Returns a random but feasable location 
    feasable_moves = list( maze_map[source_location].keys() )
    
    for neighbor in feasable_moves :
      if neighbor not in visited_locations:
        not_visited.append(neighbor)
    if not_visited == []:
      return random.choice(feasable_moves)
    else:
      return random.choice(not_visited)
       

def move_from_locations ( source_location , target_location ) : 
  difference = (target_location[0] - source_location[0], target_location[1] - source_location[1])
  if difference == (0, -1) :
    return MOVE_DOWN
  elif difference == (0, 1) :
    return MOVE_UP
  elif difference == (1, 0) :
    return MOVE_RIGHT
  elif difference == (-1, 0) :
    return MOVE_LEFT
  else :
    raise Exception("Impossible move")


##############################################################
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def preprocessing (maze_map, maze_width, maze_height, player_location, opponent_location, pieces_of_cheese, time_allowed) :
    
    # Nothing to do here
    pass



##############################################################
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# player_score : float
# opponent_score : float
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################

def turn (maze_map, maze_width, maze_height, player_location, opponent_location, player_score, opponent_score, pieces_of_cheese, time_allowed) :

    global last_position
    last_position = player_location
    # Returns a random but feasable move each turn
    target_location=random_feasable_location( maze_map , player_location )

    return move_from_locations(player_location, target_location)



