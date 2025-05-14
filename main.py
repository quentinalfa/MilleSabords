from typing import List

def tri_listes_scores_et_joueurs_par_score(scores: List[int], joueurs: List[str]):
  scores_tri: List[int] = []
  joueurs_tri: List[str] = []

  for index_non_tri in range(len(scores)):
    for index_tri in range(len(scores_tri)):
      if scores[index_non_tri] < scores_tri[index_tri]:
        scores_tri.insert(index_tri, scores[index_non_tri])
        joueurs_tri.insert(index_tri, joueurs[index_non_tri])
        break
    else:
      scores_tri.append(scores[index_non_tri])
      joueurs_tri.append(joueurs[index_non_tri])

  return scores_tri, joueurs_tri


def jouer():
    print('nouveau test')


# print (tri_listes_scores_et_joueurs_par_score([3, 4, 1, 2], ["a", "b", "c", "d"]))


