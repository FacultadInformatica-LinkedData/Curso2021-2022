# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c19PioV7eUPnYaeBqmBf2FGxYAb6nb8N

**Task 07: Querying RDF(s)**
"""

##!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
print("RDFLib query")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

print("SPARQL query")
q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person.
  }
  ''',
  initNs = { "ns": ns, "rdfs":RDFS}
)
# Visualize the results
for r in g.query(q1):
  print(r.Subject)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

print("RDFLib query")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
    print(s)
for x,y,z in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(x)

print("SPARQL query")
q1 = prepareQuery('''
  SELECT ?Subject WHERE {
     {?Subject rdf:type ns:Person.}
     UNION
     {?Subject rdfs:subClassOf ns:Person.}
  }
  ''',
  initNs = { "ns": ns}
)
# Visualize the results
for r in g.query(q1):
  print(r.Subject)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
print("RDFLib query")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  for x,y,z in g.triples((s, None, None)):
    print(x,y,z)

for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for x,y,z in g.triples((None, RDF.type, s)):
    for a,b,c in g.triples((x, None, None)):
      print(a,b,c)
    

print("SPARQL query")
q1 = prepareQuery('''
  SELECT ?s ?p ?o WHERE {
     {?s rdf:type ns:Person.
      ?s ?p ?o}
    UNION
     {?s rdf:type ?x.
      ?s ?p ?o.
      ?x rdfs:subClassOf ns:Person}
     
  }
  ''',
  initNs = { "ns": ns}
)
# Visualize the results
for r in g.query(q1):
  print(r.s, r.p, r.o)