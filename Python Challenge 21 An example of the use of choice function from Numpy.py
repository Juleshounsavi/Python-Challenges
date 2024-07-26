#An example of the use of the function np.random.choice() to simulate a football match.
import numpy as np

Pays = ["TOGO","MAROC","BENIN","NIGER"]
team1, team2, team3, team4 = np.random.choice(Pays, 4, replace=False)

print("Match 1 : {} vs {}.".format(team1, team2))
print("Match 2 : {} vs {}.".format(team3, team4))