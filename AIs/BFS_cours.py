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



def neighbors( start_vertex, graph ):
  return list( graph[start_vertex].keys() )



def traversal_BFS (structure_type, start_vertex, graph) :

  # First we create either a LIFO or a FIFO
  queuing_structure = queue.Queue()
  # Add the starting vertex with None as parent
  queuing_structure.put((start_vertex, None))
  # Initialize the outputs 
  explored_vertices = [] 
  routing_table = {} 
  # Iterate while some vertices remain

  while not queuing_structure.empty() :
  
      # This will return the next vertex to be examined, and the choice of queuing structure will change the resulting order
      (current_vertex, parent) = queuing_structure.get() 
  
      # Tests whether the current vertex is in the list of explored vertices
      if current_vertex not in explored_vertices :
          # Mark the current_vertex as explored
          explored_vertices.append(current_vertex) 
      
          # Update the routing table accordingly
          routing_table[current_vertex] = parent 
      
          # Examine neighbors of the current vertex
          for neighbor in neighbors( current_vertex , graph ) :
            # We push all unexplored neighbors to the queue
              if neighbor not in explored_vertices :              
                  queuing_structure.put((neighbor, current_vertex))          
  return routing_table



def set_path(start_vertex, finish_vertex,graph):

  #creates a stack, easier to use once moving 
  path = queue.LifoQueue()
  #initiates the stack
  path.put(finish_vertex)
  #initiats the routing table
  routing_table = traversal_BFS( path, start_vertex , graph )
  parent = finish_vertex

  #ascending the routing table from the finish point to the starting point by seeking parents
  while parent != start_vertex :
    parent = routing_table[parent]
    path.put(parent)
  #the starting point is the first element to pop, by poping it now we avoid an exception to be raised hence a dummy player
  path.get()

  return path



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
  elif difference == (0,0) :
    raise Exception("tu bouges pas") 
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
  
  #sets a path every time the rat has to move, very time consuming
  path = set_path(player_location , pieces_of_cheese[0] , maze_map )
  next_location = path.get()
  #changes the next location of the rat for the following turn
  return move_from_locations( player_location , next_location )

