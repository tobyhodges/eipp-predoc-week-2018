# Predoc Week Git Session

#### Recap

- mkdir horsing-around
- cd
- git init
- make readme
  - add, commit, git log, reset
- GitHub
  - create repo
- add remote
- pull
- edit, add, commit, push

#### Branches, Merging

- git checkout -b new_branch
- make some changes, commit
- switch back to master
  - git checkout master
- and back again to new_branch
- make some more changes, add but don't commit
- try to switch back to master
- git stash
- git checkout master
- git checkout new_branch
- git stash pop
- commit, push
- git checkout master
- git diff master new_branch
- git merge new_branch
- slides
- show how to protect a branch
- now do it online
- pair up, add to each other's repository
- Pull Request exercise

#### Coffee Break?

#### Continuous Integration

- copy pubmed results and listing script into repo - script in `src/`
- add, commit
- run script, look at output
- add, commit
- write some tests, save in `src/`
- log into Travis
- add repository to Travis
- add Markdown of status report to README
- write .travis.yml file

```
language: "python"
python:
-   "3.6"
# install:
# -   "pip install -r requirements.txt"
script:
-   "pytest src/test_markdown.py"
```

requirements.txt:
```
pytest
```

- commit, look at logging in Travis
- fix code
- commit, look at logging in Travis
- celebrate!
- note that CI is for more than 'just' automated testing
  - could use it to generate .md files by year in the GH Pages part below...

#### GitHub Pages

- activate publising
- make listing, write to index.md
- go to URL
- add a title to index.md
- make contact.md
- disable by adding a .nojekyll file (works for individual directories)
- will also start building automatically from a directory called 'docs'

More on using Jekyll to publish material with GitHub Pages
https://help.github.com/categories/customizing-github-pages/
