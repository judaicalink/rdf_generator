from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import FOAF, DC


class RDFBuilder:
    def __init__(self):
        self.graph = Graph()
        self.ns = Namespace("http://example.org/ns#")

    def add_person(self, name, email):
        person = URIRef(f"http://example.org/person/{name.replace(' ', '_')}")
        self.graph.add((person, FOAF.name, Literal(name)))
        self.graph.add((person, FOAF.mbox, URIRef(f"mailto:{email}")))

    def serialize(self, format="turtle"):
        return self.graph.serialize(format=format).decode("utf-8")
