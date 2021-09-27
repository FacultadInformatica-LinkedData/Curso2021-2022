#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[17]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[18]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[24]:



#RDFLib
ns = Namespace("http://somewhere#")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

#SPARQL
from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
PREFIX ns:<http://somewhere#>
SELECT DISTINCT ?subclass
WHERE {
 ?subclass rdfs:subClass ns:Person
  }
  '''
)
for r in g.query(q1):
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[46]:


#RDFLib
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for a,b,c in g.triples((None, RDF.type, s)):
   print(a)

#SPARQL
q2 = prepareQuery('''
PREFIX ns:<http://somewhere#>
SELECT DISTINCT ?individual
WHERE {
 ?class rdfs:subClass ns:Person .
 ?individual rdf:type ?class 
  }
  '''
)
for r in g.query(q2):
  print(r)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[47]:


#RDFLib
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for a,b,s in g.triples((None, RDF.type, s)):
    for a,c,d in g.triples((a, None, None)):
     print(a,c,d)
#SPARQL
q3 = prepareQuery('''
PREFIX ns:<http://somewhere#>
SELECT DISTINCT ?individual ?prop ?prop2
WHERE {
 ?class rdfs:subClass ns:Person .
 ?individual rdf:type ?class .
 ?individual ?prop ?prop2
 
  }
  '''
)
for r in g.query(q3):
  print(r)


# In[ ]:




