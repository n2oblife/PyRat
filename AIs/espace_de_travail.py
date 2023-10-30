# %%
##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################


MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'


##############################################################
# Please put your code here (imports, variables, functions...)
##############################################################



import queue

routing_table = {} 
explored_locations = []
path = queue.LifoQueue()
 


def give_all_neighbours( maze_map , player_location ):
  return list( maze_map[player_location].keys() )



def give_unexplored_neighbours( maze_map , player_location ):
  
  global explored_locations
  not_visited=[]
  neighbours = []

  neighbours = give_all_neighbours( maze_map , player_location )

  for element in neighbours:
    if element not in explored_locations :
      not_visited.append(element)
  
  return not_visited



def update_queue( waiting_queue , neighbours , source_location ):
  #remplir une liste d'attente automatiquement pour 
  
  for element in neighbours :
    waiting_queue.put(( element , source_location )) #faire attention, car on verifie deja si ils ont ete exploré dans la fonction après
  
  pass



def set_routing_table_BFS( maze_map , player_location ):
  #donne en BFS le dico des parents de chaque element
  #possible à améliorer pour avoir une recherche vers le fromage le plus court

  global routing_table #quand on aura plusieurs fromage il faudra vider cette liste à l'arrivée au fromage avec cette nouvelle racine
  global explored_locations
  
  parent_relation = ()
  waiting_queue = queue.Queue()

  routing_table.update({ player_location : None })
  explored_locations.append(player_location)
 
  unexplored = give_unexplored_neighbours( maze_map , player_location ) #possible de donner tous les voisins car on vérifie ensuite si ils ont deja ete explorés
  update_queue( waiting_queue , unexplored , player_location )

  '''
  for neighbour in give_unexplored_neighbours( maze_map , player_location ):
    waiting_queue.put(( neighbour , player_location ))
  '''

  while not waiting_queue.empty() :
    parent_relation = waiting_queue.get()
    if parent_relation[0] not in explored_locations :
      routing_table.update({ parent_relation[0] : parent_relation[1] })
      unexplored = give_unexplored_neighbours( maze_map , parent_relation[0] )
      update_queue( waiting_queue , unexplored , parent_relation[0] )
  
  pass



def set_path( finish_point ):
  #returns a list of the place to go

  global routing_table
  global path

  path.put(finish_point)
  parent_relation = routing_table[ finish_point ]
  
  while parent_relation[1]!= None :
    parent_relation = routing_table.get( parent_relation[1] )
    path.put( parent_relation[0] )
  
  pass



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
  elif difference == (0,0):
    raise Exception("meme position")      
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
  
  set_routing_table_BFS( maze_map , player_location )
  set_path( routing_table , pieces_of_cheese[0] )

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

  global path
  
  if not path.empty():
    next_location = path.get()
    return move_from_locations( player_location , next_location )

  else :
    raise Exception("Impossible move")


