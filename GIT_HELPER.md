# 📦 Guide rapide Git

Je t'ai enlevé le dossier MilleSabords donc le projet commence à la racine ;)
``` bash
~/workspace$ <commande>
```

## 📝 Ajouter et versionner tes fichiers

1. Ajouter un fichier :

``` bash
git add <nom_du_fichier>
```

2. Commit :

``` bash
git commit -m "Ton message commit"
```

## 🚀 Envoyer tes modifications

``` bash
git push origin main
```
Si tu travaille sur une autre branche remplace ___main___ par son nom.

## 🔄 Récupérer les mises à jour

``` bash
git pull origin main
```

De meme, adapte ___main___ si nécessaire

## 🌱 Créer une nouvelle branche

``` bash
git branch nom_de_branche
```

## 🛠 Travailler sur ta branche

``` bash
git checkout nom_de_branche
```

## 🚀 Pousser ta branche pour la première fois

``` bash
git push --set-upstream origin nom_de_branche
```

## 📤 Pour les prochains push/pull

``` bash
git push
git pull
```

Git saura vers quelle branche distante pousser ou tirer.

## 🌳 Voir les branches existantes

``` bash
git branch
```
Affiche les branches locales. L’étoile * indique celle sur laquelle tu es actuellement.

Pour voir aussi les branches distantes :
``` bash
git branch -r
```

## 🧹 Supprimer une branche locale
``` bash
git branch -d nom_de_branch
```

## 🔀 Fusionner une branche (merge)

Une fois que tu as terminé ton travail dans une branche (par exemple feature/truc), tu peux fusionner cette branche dans main :

1. Revenir sur la branche cible (main, le plus souvent) :
``` bash
git checkout main
```
2. Fusionner la branche de travail :
``` bash
git merge feature/truc
```
Cela applique les changements de feature/truc dans main.

4. Pousser les changements :
``` bash
git push origin main
```
👉 Si un conflit apparaît, Git t'indiquera les fichiers à résoudre. Tu devras modifier les fichiers conflictuels à la main, puis faire :
``` bash
git add <fichiers_modifiés>
git commit
```

## 🔃 Récupérer les mises à jour (sans merge automatique)
``` bash
git fetch origin
```
Cette commande récupère toutes les mises à jour distantes, sans les fusionner dans tes branches locales.

C’est utile si tu veux :

- Voir ce qui a changé sur le dépôt distant,
- Comparer les branches locales/distant,
- Fusionner manuellement après inspection.