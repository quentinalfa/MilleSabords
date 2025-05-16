from utils import tri_listes_scores_et_joueurs_par_score as tri

def jouer():
  goal = 6000
  players = []
  scores = []
  current_player_index = 0

  nb_players = int(input("combien y a t'il de joueur ? "))
  print()

  for i in range(nb_players) :
    players.append(input('quel est le nom du joueur ' + str( i+1 ) + '? ')) 
    scores.append(0)

  print()

  while scores[current_player_index] < goal :
    scores[current_player_index] += int(input(players[current_player_index] + " à gagner combien de points ? "))
    print(players[current_player_index],"à",scores[current_player_index],"de scores")
    current_player_index = (current_player_index +1) %nb_players
    print()

  scores_tri, joueurs_tri = tri(scores, players)

  print("1 ère place :", joueurs_tri[0], "(score :",scores_tri[0],")")
  for i in range(1, len(scores_tri)):
    print(i+1,"ème place :", joueurs_tri[i], "(score :",scores_tri[i],")")

