# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kChotAXHgmBlK1bGd1GvccvgYNO6Ae-1

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
ns = Namespace("http://somewhere#")
from rdflib.plugins.sparql import prepareQuery
q1=prepareQuery('''
SELECT ?entity WHERE{
  ?entity rdfs:subClassOf ns:Person
}
''',
initNs = {"rdfs" : RDFS, "ns" : ns}    
)
# Visualize the results
print("WITH RDFLIB")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)
print("WITH SPARQL")
for r in g.query(q1):
  print(r.entity)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery("""
SELECT ?entity WHERE {
  {?entity rdf:type ns:Person.}
  UNION{
    ?sub rdfs:subClassOf ns:Person.
    ?entity rdf:type ?sub.}
}
""", initNs = {"rdf": RDF, "rdfs": RDFS, "ns": ns })

# Visualize the results
print("WITH RDFLIB")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for sub, x, y in g.triples((None, RDF.type, s)):
        print(sub)
print("WITH SPARQL")
for r in g.query(q2):
  print(r.entity)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
q3 = prepareQuery("""
  SELECT ?s ?p ?o WHERE { 
    { 
      ?s rdf:type ns:Person.
      ?s ?p ?o.}
    UNION{
        ?sub rdfs:subClassOf ns:Person.
        ?s rdf:type ?sub.
        ?s ?p ?o}
  }
  """,initNs = {"rdf": RDF, "rdfs": RDFS, "ns": ns })
# Visualize the results
print("WITH RDFLIB")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for s2, p2, o2 in g.triples((s, None, None)):
        print(s2, p2, o2)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2, p2, o2 in g.triples((None, RDF.type, s)):
        for s3, p3, o3 in g.triples((s2, None, None)):
            print(s3, p3, o3)

print("WITH SPARQL")
for r in g.query(q3):
  print(r.s, r.p, r.o)