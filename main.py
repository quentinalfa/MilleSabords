from mille_sabords import jouer

def main () :
  envie_de_jouer = True

  while envie_de_jouer :
    jouer()
    print()
    rejouer = input('vous voulez rejouez ? (y/n) ')
    print()
    if rejouer == "n" :
      envie_de_jouer = False
      
if __name__ == '__main__':
  main()

