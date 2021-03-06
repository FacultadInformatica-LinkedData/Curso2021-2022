# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tV5j-DRcpPtoJGoMj8v2DSqR_9wyXeiE

**Task 07: Querying RDF(s)**
"""

"""!pip install rdflib"""
from rdflib.plugins.sparql import prepareQuery

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/course_materials/rdf/example6.rdf", format="xml")

ns = Namespace("http://somewhere#")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL** """

#RDFlib
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)

#SPARQL
q1 = prepareQuery('''
    SELECT ?Subject WHERE{
        ?Subject rdfs:subClassOf ns:Person.
    }''',
    initNs = {"ns":ns}
    )

for r in g.query(q1):
    print(r.Subject)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""

#RDFlib

for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2, p, o in g.triples((None, RDF.type, s)):
        print(s2)

#SPARQL

q2 = prepareQuery('''
    SELECT ?Subject WHERE{
        ?Subject rdf:type ns:Person.
        ?Sc rdfs:subClassOf ns:Person.
        ?Subject rdf:type ?Sc.
    }''',
    initNs={"ns": ns}
    )

for r in g.query(q2):
    print(r.Subject)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""

# RDFlib

for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for s2, p2, o in g.triples((s, None, None)):
        print(s2, p2)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2, p2, o in g.triples((None, RDF.type, s)):
        for s3, p3, o in g.triples((s, None, None)):
            print(s, p3)


# SPARQL

q3 = prepareQuery('''
    SELECT ?Subject ?Predicate ?Object WHERE{
        ?Subject rdf:type ns:Person.
        ?Sc rdfs:subClassOf ns:Person.
        ?Subject rdf:type ?Sc.
        ?Subject ?Predicate ?Object.
    }''',
    initNs={"ns": ns}
    )

for r in g.query(q3):
    print(r.Subject, r.Predicate, r.Object)
