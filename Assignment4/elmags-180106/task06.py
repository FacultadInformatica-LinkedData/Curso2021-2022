# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18UQSVF5Fef6NeRY8keHQbtMQ-SIO0ULZ

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

ns = Namespace("http://somewhere#")

"""Create a new class named Researcher"""

g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

janeURI = ns.JaneSmith

g.add((janeURI, RDF.type, ns.Researcher))

for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

fullName = Literal("Jane Smith")
given = Literal("Jane")
family = Literal("Smith")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

resource1 = (janeURI, VCARD.Researcher, fullName)
resource2 = (janeURI, VCARD.Given, given)
resource3 = (janeURI, VCARD.Family, family)

g.add(resource1)
g.add(resource2)
g.add(resource3)

for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

from rdflib import FOAF
upmURI = ns.UPM
upmName = Literal("UPM")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

resource4 = (upmURI, VCARD.University, upmName)

g.add((upmURI, RDF.type, ns.University))
g.add((ns.JohnSmith, ns.Works, upmURI))
g.add(resource4)

for s, p, o in g:
  print(s,p,o)