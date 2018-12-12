# MathGenGraph
Create a genealogy graph for a scientist on [Mathematics Genealogy Project](https://www.genealogy.math.ndsu.nodak.edu).

## Dependencies
Make sure the following dependencies are installed:
```
pip install requests beautifulsoup4 lxml graphviz
```
**For Windows users:** You might encounter some troubles when rendering the dot representation of the graph to a pdf. The answer to [this stackoverflow post](https://stackoverflow.com/a/44005139) might help.


## Instructions
Clone the repo:
```
git clone https://github.com/pedrozudo/MathGenGraph.git
```
Figure out who you want to stalk. Therefore, go to the website, search for the scientists in whose academic genealogy you are interested, and from the url get the ID. For example, for [Lise Meitner](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=110960) you would have the following url.
```
https://www.genealogy.math.ndsu.nodak.edu/id.php?id=110960
```
The ID is then the last part of the address: `110960`.

Once you know this, you are ready:
```
cd MathGenGraph
python mathgengraph/mathgengraph.py 110960
```
Most of the time is spent on scraping the website. The name of the "currently scraped" scientist is printed out to the terminal.

In `mathgengraph/digrams` you can now find the file `110960.pdf`. [Here is the result](https://github.com/pedrozudo/MathGenGraph/blob/master/mathgengraph/diagrams/110960.gv.pdf).
