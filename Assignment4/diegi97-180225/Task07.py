#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[5]:


from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

tupSubclasses = (None, RDFS.subClassOf, ns.Person)

for s, p, o in g.triples(tupSubclasses):
     print(s)

q1 = prepareQuery('''
SELECT ?v WHERE{
     ?v rdfs:subClassOf ns:Person
}
''', initNs={"rdfs":RDFS, "ns":ns})

for r in g.query(q1):
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[23]:


print('7.2 RDFLIB:')
for sub, pred, obj in g.triples((None, None, ns.Person)):
    if pred == RDFS.subClassOf:
        for sub2, pred2, obj2 in g.triples((None, RDF.type, sub)):
            print(sub2)
    elif pred == RDF.type:
        print(sub)

print('7.2 SPARQL:')

q2 = prepareQuery('''
SELECT ?v WHERE {{
    ?v rdf:type ns:Person .

} UNION
{
    ?v rdf:type ?p .
    ?p rdfs:subClassOf ns:Person
}}''', initNs={"rdfs":RDFS, "rdf":RDF, "ns":ns})

for r in g.query(q2):
  print(r)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[42]:


print('7.3 RDFLIB:')
for sub, pred, _ in g.triples((None, None, ns.Person)):
    if pred == RDFS.subClassOf:
        for sub2, _, _ in g.triples((None, RDF.type, sub)):
            print(sub2)
            for sub3, pred3, obj3 in g.triples((sub2, None, None)):
                print(pred3, obj3)
    elif pred == RDF.type:
        print(sub)
        for sub4, pred4, obj4 in g.triples((sub, None, None)):
            print(pred4, obj4)
        

print('7.3 SPARQL:')

q3 = prepareQuery('''
SELECT ?v ?p ?o WHERE {{
    ?v rdf:type ns:Person .
    ?v ?p ?o
} UNION
{
    ?v rdf:type ?pp .
    ?pp rdfs:subClassOf ns:Person .
    ?pp ?p ?o
}}''', initNs={"rdfs":RDFS, "rdf":RDF, "ns":ns})

for r in g.query(q3):
  print(r)

