# [WIP] Bugs-Annoy!
Detecting buggy code from the Bug description.

Python based project to find Potential buggy lines of code in any Github repository by just entering the bug       description.

## Installation
```
#Install PyQT4
$ sudo apt-get install python-qt4

# Install tkinter
$ apt-get install python-tk 

$ git clone https://github.com/satwikkansal/Bugs-Annoy.git
$ cd Bugs-Annoy
$ pip install -r requirements.txt
$ python gui.py

```
**Note:** Currently this project works only on Eclipse Project which you can also find in this repository. The support for any github repsitory will be added soon!

## Stage 1 Milestones:
- Setup and UI in PyQT4 [x]
- Implement Lexical Similarity b/w Source code and bug description [x]
- Test it on a standard Issues Dataset (Eclipse IDE) [x]
- Generalize it to be used on any Github Repository (WIP)
- Support to synchronize API docs to improve the accuracy of predictor.

## Stage 2 Milestones:

I've not come up with the exact model yet but it involves use of Machine Learning and Multi-Objective Search Algorithms to improve the accuracy of the results produced by simple lexical similarity function in the Stage 1. I'm planning to consider the similarity in b/w bugs and similarity in b/w source code separately (like a bi-partite graph) and then using some algorithm like Random Walk that utilizes previous bug descriptions and version control history to associate the newly created bug description with a specific part of the source code.

The model takes into account several other factors like
- Version Control History
- Recency of changes in the files
- Comments are given more weightage
- API Documentation
- Language dependent preprocessing/parsing of the source code.

## Current Progress

It's not very accurate, but it's better than nothing :P

![Alt text](/screenshots/Screenshot-stage1.png?raw=true "Stage 1")


