# Set Up Git Repo

1. create a new repository on the command line:

   - echo "# calculator-mcp" >> README.md
   - git init
   - git add README.md
   - git commit -m "first commit"
   - git branch -M main
   - git remote add origin https://github.com/rubensgomes/calculator-mcp.git
   - git push -u origin main

2. push an existing repository from the command line:

   - git remote add origin https://github.com/rubensgomes/calculator-mcp.git
   - git branch -M main
   - git push -u origin main

3. this is how Rubens initialized other projects in GIT:

   - PROJ_NAME=calculator-mcp
   - git init -b main
   - git add .
   - git commit -m "initial commit" -a
   - gh repo create --homepage "https://github.com/rubensgomes" --public "${PROJ_NAME}"
   - git remote add origin "https://github.com/rubensgomes/${PROJ_NAME}"
   - git push -u origin main


