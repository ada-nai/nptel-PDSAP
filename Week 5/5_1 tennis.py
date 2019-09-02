
#Problem 5.1
stats = {}
while(True):
    # Take input from console
    match = input()
    #match = input("Input:")
    # Terminate if newline
    if match == "":
        break
    else:
        # Split the input to get names and scorecard of match
        result = match.split(':')
        #print(type(result[2]))
        #Split the result list to check if 3 or 5 set match
        score_str = result[2].split(',')
        # Check if the player name is present in stats dic, if not add them with required parameters
        if result[0] not in stats.keys():
            stats[result[0]] = {'w_5':0, 'w_3':0, 'w_sets':0, 'w_games':0, 'l_sets' :0, 'l_games':0}
        if result[1] not in stats.keys():
            stats[result[1]] = {'w_5':0, 'w_3':0, 'w_sets':0, 'w_games':0, 'l_sets' :0, 'l_games':0}
        if len(score_str) <= 3:
            stats[result[0]]['w_3'] += 1
        else:
            stats[result[0]]['w_5'] += 1 
        
        #Evaluate the set/game stats by splitting scores

        #Get the scores in the form of individual strings
        score_list = []
        for item in score_str:
            score_list.extend(item.split('-'))

        #Convert string of numbers to int
        score_li = []
        for item in score_list:
            score_li.append(int(item))

        #Get desired structure of set as list of list of int
        fin_set = [score_li[i:i+2]for i in range(0,len(score_li),2)]

        # Compute sets won 
        f_s_w = 0 #first player sets won
        s_s_w = 0 #second player sets won
        for item in fin_set:
            if item[0]>item[1]:
                f_s_w +=1
            else:
                s_s_w +=1
        #(f_s_w, s_s_w)
        stats[result[0]]['w_sets'] += f_s_w
        stats[result[0]]['l_sets'] += s_s_w
        stats[result[1]]['w_sets'] += s_s_w
        stats[result[1]]['l_sets'] += f_s_w

        # Compute games won/lost
        f_g_w = 0 #first player games won
        s_g_w = 0 #second player games won 
        for item in fin_set:
             f_g_w += item[0]
             s_g_w += item[1]

        stats[result[0]]['w_games'] += f_g_w
        stats[result[0]]['l_games'] += s_g_w
        stats[result[1]]['w_games'] += s_g_w
        stats[result[1]]['l_games'] += f_g_w
    
#Print out the result as desired
#Though the stats dict is computed, it is still not sorted,
# hence the key values are appended to a list of list 
stats_list = []
ite = 0
for item in stats.keys():
    #print(item, end = " ")
    stats_list.append([item])
    for stat in stats[item]:
        #print(stats[item][stat],end = " ")
        stats_list[ite].append(stats[item][stat]) 
        #We need only root values and the main key 
        #i.e stats and main key(name of player)
    ite +=1 # iterator to append as a new element in the list
#print(stats_list)
 
#define key for the sort function

'''alternative to the lambda function
def custom(li):
    return li[1:len(li)-2] #last two keys are to be sorted as ascending
'''

fin_list = sorted(stats_list, key = lambda x: x[1:len(x)-2] ,reverse = True)

#Finally obtain the stats as required
for item in fin_list:
    for ele in item:
        print(ele,end = " ")
    print()
#print(fin_list)