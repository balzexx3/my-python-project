from main import add
def test_add():
assert add(3, 4) == 7
assert add(-1, 1) == 0
assert add(0, 0) == 0
4. Initialisez votre dépôt Git :
git init
git add .
git commit -m "Initial commit"
git remote add origin <URL_DE_VOTRE_REPOSITORY>
git push -u origin master
