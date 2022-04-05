# Question 2 CCC

N = int(input()) 
Stars = 0

for i in range (N):
    Points = int(input()) *5 
    Fouls = int(input()) *3 
    DifferenceOfPointsAndFouls = Points - Fouls
    if DifferenceOfPointsAndFouls > 40:
        Stars = Stars + 1 

if Stars == N:
    print(str(Stars), "+")
else:
    print(str(Stars))
    


 



        