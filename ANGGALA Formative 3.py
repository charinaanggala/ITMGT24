#!/usr/bin/env python
# coding: utf-8

# # Programming Set 3
# 
# ## Assignment will develop your ability to manipulate data.

# In[3]:


def relationship_status(from_member, to_member, social_graph):
    relationship = ""
    member_details = social_graph.get(from_member)
    from_follows_to = to_member in member_details.get('following')

    member_details2 = social_graph.get(to_member)
    to_follows_from = from_member in member_details2.get('following')

    

    if from_follows_to == True and to_follows_from == True:
        relationship = "friends"
    elif from_follows_to == True and to_follows_from == False:
        relationship = "follower"
    elif from_follows_to == False and to_follows_from == True:
        relationship = "followed by"
    else :
        relationship = "no relationship"                
    return relationship 


# In[5]:


def tic_tac_toe(board):
    result = "NO WINNER"
    #horizontal
    for j in range(len(board)): 
        if board[j].count("X") == len(board):
            return "X" 
        elif board[j].count("O") == len(board):
            return "O"
   
    #vertical
    vertical =""
    for j in range(len(board)):
        for i in range(len(board)):
            vertical += board[i][j]
        if vertical == "X"*len(board):
            return "X"
        elif vertical == "O"*len(board):
            return "O"
        vertical = ""
  
    #diagonal
    diagonal = ""
    i=0
    for k in range(len(board)): 
        diagonal += board[k][k] 
    if diagonal == "X"*len(board):
        return "X"
    elif diagonal == "O"*len(board):
        return "O"
   
    #antidiagonal
    antidiagonal = ""
    i = 0
    for k in range(len(board)): 
        antidiagonal += board[k][len(board)-1-k] 
        i = i + 1
        k = k + 1
        
    if antidiagonal == "X"*len(board):
        return "X"
    elif antidiagonal == "O"*len(board):
        return "O"
    
    return result
        


# In[7]:


def eta(first_stop, second_stop, route_map):
    From_ = list(route_map.keys())
    arrived = False 
    current_stop = first_stop
    Total_traveltime = 0 
    
    while arrived == False:
        for i in range(len(route_map)):
            locations = list(From_[i])
            if locations[0] == current_stop:
                key = From_[i]
                travel_time = route_map.get(key)
                if key !="":
                    Route = travel_time["travel_time_mins"] 
                else:
                    Route = 0
                Total_traveltime += Route
                if locations[1] == second_stop:
                    arrived = True
                    return Total_traveltime
                elif locations[1] != second_stop:
                    current_stop = locations[1]

