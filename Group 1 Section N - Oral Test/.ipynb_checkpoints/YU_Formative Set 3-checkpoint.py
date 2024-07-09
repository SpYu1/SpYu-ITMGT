'''
Sample data for Relationship Status below:
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    follower = to_member in social_graph[from_member]['following']
    followed_by = from_member in social_graph[to_member]['following']

    if follower and followed_by:
        status = "friends"
    elif follower:
        status = "follower"
    elif followed_by:
        status = 'followed by'
    else:
        status = 'no relationship'

    return status

'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

board8 = [
['X','X','O',''],
['O','X','O','O'],
['O','','','O'],
['O','X','','']
]


def tic_tac_toe(board):
    '''Evaluates a tic tac toe board and returns the winner or "NO WINNER" if there is none.'''
    n = len(board)  
    
    # Check Rows and Columns
    for i in range(n):
        # Check Row i
        row_incorrect = False 
        for j in range(n):
            if board[i][0] != board[i][j]:
                row_incorrect = True
                
        if len(board[i][0]) > 0 and not row_incorrect:
            return board[i][0]
            

        # Check Column i
        column_incorrect = False
        for j in range(n):
            if board[0][i] != board[j][i]:
                column_incorrect = True
        
        if len(board[0][i]) > 0 and not column_incorrect:
            return board[0][i]

    # Check Diagonals
    # Top Left to Bottom Right
    diagonal_incorrect_1 = False
    for i in range(n):
        if board[n-1][n-1] != board[i][i]:
            diagnoal_incorrect_1 = True

    if len(board[n-1][n-1]) > 0 and not diagonal_incorrect_1:
        return board[n-1][n-1]


    # Top Right to Bottom Left
    diagonal_incorrect_2 = False
    for i in range(n):
        if board[0][n-1] != board[i][n-(1+i)]:
            diagonal_incorrect_2 = True

    if len(board[0][n-1]) > 0 and not diagonal_incorrect_2:
        return board[0][n-1]
        
    return "NO WINNER"

'''
Sample data for ETA below:

(from_stop, to_stop)
'''
legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'b2'): {
        'travel_time_mins': 1
    },
    ('b2', 'a1'): {
        'travel_time_mins': 5
    }
}

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    dict_keys =list(route_map.keys())
    
    start_keys = []
    end_keys = []


    for item in range(len(dict_keys)):
        start_keys.append(dict_keys[item][0])
        end_keys.append(dict_keys[item][1])

    start_point = start_keys.index(first_stop)
    end_point = end_keys.index(second_stop)

    num_list = []

    if start_point == end_point:
        key = (first_stop, second_stop)
        return route_map[key]['travel_time_mins']
    
    elif start_point < end_point:
        for item in range(start_point, end_point+1):
            num_list.append(route_map[dict_keys[item]]['travel_time_mins'])
        
    elif start_point > end_point:
        for item in range(start_point, len(dict_keys)):
            num_list.append(route_map[dict_keys[item]]['travel_time_mins'])

        for item in range(0, end_point+1):
            num_list.append(route_map[dict_keys[item]]['travel_time_mins'])


    sum = 0        
    for item in range(len(num_list)):
        sum += num_list[item]
    
    return sum