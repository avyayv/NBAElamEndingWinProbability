# ElamEndingWinProbability
This is some of the code behind my blog post https://analyzeball.com/2020/03/15/elam-ending-analytics/.

You can find win probabilities by running the following command

`python winp.py scoreX scoreY`

```
usage: winp.py [-h] scoreX scoreY

Win Probabilities in OT

positional arguments:
  scoreX      Score for the team with possession
  scoreY      Score for the team without possession

optional arguments:
  -h, --help  show this help message and exit
  
```

It will return results like so

```
Probability of team with possession winning is ....
Probability of team without possession winning is ....
```
