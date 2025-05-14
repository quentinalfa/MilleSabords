from typing import List

def tri_listes_scores_et_joueurs_par_score(scores: List[int], joueurs: List[str]):
  scores_tri: List[int] = []
  joueurs_tri: List[str] = []

  for index_non_tri in range(len(scores)):
    for index_tri in range(len(scores_tri)):
      if scores[index_non_tri] > scores_tri[index_tri]:
        scores_tri.insert(index_tri, scores[index_non_tri])
        joueurs_tri.insert(index_tri, joueurs[index_non_tri])
        break
    else:
      scores_tri.append(scores[index_non_tri])
      joueurs_tri.append(joueurs[index_non_tri])

  return scores_tri, joueurs_tri


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

  scores_tri, joueurs_tri = tri_listes_scores_et_joueurs_par_score(scores, players)

  print("1 ère place :", joueurs_tri[0], "(score :",scores[0],")")
  for i in range(1, len(scores_tri)):
    print(i+1,"ème place :", joueurs_tri[i], "(score :",scores[i],")")





jouer ()
# print (tri_listes_scores_et_joueurs_par_score([3, 4, 1, 2], ["a", "b", "c", "d"]))

