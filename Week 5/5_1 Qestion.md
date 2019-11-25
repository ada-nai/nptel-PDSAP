 Here are some basic facts about tennis scoring: A tennis match is made up of sets. A set is made up of games.

To win a set, a player has to win 6 games with a difference of 2 games. At 6-6, there is often a special tie-breaker. In some cases, players go on playing till one of them wins the set with a difference of two games.

Tennis matches can be either 3 sets or 5 sets. The player who wins a majority of sets wins the match (i.e., 2 out 3 sets or 3 out of 5 sets) The score of a match lists out the games in each set, with the overall winner's score reported first for each set. Thus, if the score is 6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost the second one 5 games to 7 and won the third one 7 games to 6 (and hence won the overall match as well by 2 sets to 1).

You will read input from the keyboard (standard input) containing the results of several tennis matches. Each match's score is recorded on a separate line with the following format:

Winner:Loser:Set-1-score,...,Set-k-score, where 2 ≤ k ≤ 5

For example, an input line of the form

Halep:Wozniacki:3-6,6-3,6-3

indicates that Halep beat Wozniacki 3-6, 6-3, 6-3 in a best of 3 set match.

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches and compile the following statistics for each player:
```
    Number of best-of-5 set matches won
    Number of best-of-3 set matches won
    Number of sets won
    Number of games won
    Number of sets lost
    Number of games lost 
```

You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the criteria 1-6 in that order (compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).

For instance, given the following data
```
Federer:Nadal:2-6,6-7,7-6,6-3,6-1
Nadal:Federer:6-3,4-6,6-4,6-3
Federer:Nadal:6-0,7-6,6-7,6-3
Nadal:Federer:6-4,6-4
Federer:Nadal:2-6,6-2,6-0
Nadal:Federer:6-3,4-6,6-3,6-4
Federer:Nadal:7-6,4-6,7-6,2-6,6-2
Nadal:Federer:7-5,7-5
Halep:Wozniacki:3-6,6-3,6-3
```
your program should print out the following
```
Federer 3 1 13 142 16 143
Nadal 2 2 16 143 13 142
Halep 0 1 2 15 1 12
Wozniacki 0 0 1 12 2 15
```
You can assume that there are no spaces around the punctuation marks ":", "-" and ",". Each player's name will be spelled consistently and no two players have the same name. 
