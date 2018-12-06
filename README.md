# MathGenGraph
Create a genealogy graph for a scientist on [Mathematics Genealogy Project](https://www.genealogy.math.ndsu.nodak.edu)

## Instructions
Clone the repo:
```
git clone https://github.com/pedrozudo/MathGenGraph.git
```
Figure out who you want to stalk. Therefore to the website, search for the scientists in whose academic genealogy you are interested and from the url get the ID. For example for [Lise Meitner](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=110960) you would have the following url.
```
https://www.genealogy.math.ndsu.nodak.edu/id.php?id=110960
```
The ID is then the last part of the address: `110960`.

Once you know this, you are ready:
```
cd MathGenGraph
python mathgengraph/mathgengraph.py 110960
```
In `mathgengraph.digrams` you can now find the file `110960.pdf`. Open it.
