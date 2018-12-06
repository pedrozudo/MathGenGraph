import sys
import os
import pickle
import requests
from bs4 import BeautifulSoup
from graphviz import Source



WEBSITE_TRUNK = "https://www.genealogy.math.ndsu.nodak.edu/id.php?id="
PATH_NAME = os.path.dirname(os.path.abspath(__file__))


class Graph(object):
    def __init__(self, scientist_id):
        self.scientist_id = scientist_id
        self.id2name = {}
        self.id2year = {}
        self.advisors = {}
        self.build_graph(scientist_id)

    def build_graph(self, scientist_id):
        dump_file_name = os.path.join(PATH_NAME,"graphs", self.scientist_id)
        if os.path.isfile(dump_file_name):
            with open(dump_file_name, 'rb') as dump_file:
                graph = pickle.load(dump_file)
                self.scientist_id = graph.scientist_id
                self.id2name = graph.id2name
                self.id2year = graph.id2year
                self.advisors = graph.advisors
        else:
            self._build_graph(self.scientist_id)
            with open(dump_file_name, 'wb+') as dump_file:
                pickle.dump(self, dump_file)

    def _build_graph(self, scientist_id):
        if scientist_id in self.id2name:
            pass
        else:
            req = requests.get(WEBSITE_TRUNK+scientist_id)
            soup = BeautifulSoup(req.text, "lxml")

            scientist_name = soup.find_all("h2")[0].text.strip("\n").strip(" ")
            scientist_year = soup.find('div', attrs={'style':'line-height: 30px; text-align: center; margin-bottom: 1ex'})
            scientist_year = scientist_year.find_all('span')[0].contents[-1].strip(" ")
            print(scientist_name)

            self.id2name[scientist_id] = scientist_name
            self.id2year[scientist_id] = scientist_year

            paragraphs = soup.find_all("p")
            advisors = [p for p in paragraphs if "Advisor" in p.text][0]
            advisors = advisors.find_all("a")
            self.advisors[scientist_id] = []
            for a in advisors:
                a_id = a.attrs["href"].split("id=")[1]
                self.advisors[scientist_id].append(a_id)
                self._build_graph(a_id)



    def graph2dot(self):
        dot_string = self._to_dot()
        g = Source(dot_string)
        diagram_name = os.path.join(PATH_NAME,'diagrams,{}.gv').format(self.scientist_id)
        g.render(diagram_name, view=False)

    def _to_dot(self):
        s = 'digraph GP {\n'
        s = self._add_node(s, self.scientist_id)
        s += "}"
        return s

    def _add_node(self, s, scientist_id, parents=[]):

        for a_id in self.advisors[scientist_id]:
            if not a_id+" [label" in s:#hack
                s = self._add_node(s, a_id)
                s += '{scientist_id} -> {a_id} [dir=back];\n'.format(scientist_id=scientist_id, a_id=a_id)

        s += '{scientist_id} [label="{scientist_name}\n{scientist_year}", shape="ellipse", style="filled", fillcolor="white"];\n'.\
            format(scientist_id=scientist_id, scientist_name=self.id2name[scientist_id], scientist_year=self.id2year[scientist_id])
        return s



if __name__ == "__main__":
    python_version = sys.version_info
    if python_version[0]==2:
        print("God damn it, use python3!")
    else:
        scientist_id = sys.argv[1]

        scientist_graph = Graph(scientist_id)
        scientist_graph.graph2dot()
