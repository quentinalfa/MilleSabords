def save_scores(scores_tri, players_tri):
    with open("scores.txt", "w") as scores_file :
      for i in range(len(scores_tri)):
        scores_file.write(players_tri[i] + " : " + str(scores_tri[i])+"\n")
