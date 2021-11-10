    #!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[2]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[3]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[11]:


# TO DO
# Visualize the results

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s,p,o)

q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "ns": ns}
)
for r in g.query(q1):
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[13]:

ns= Namespace("http://somewhere#")
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  # print(s,p,o)
  for s,p,o in g.triples((None,RDF.type,s)):
    print(s,p,o)
for s,p,o in g.triples((None,RDF.type,ns.Person)):
  print(s,p,o)
  
 
from rdflib.plugins.sparql import prepareQuery 
q2 = prepareQuery('''
    SELECT ?s WHERE { 
    ?x rdfs:subClassOf* ns:Person.
    ?s rdf:type ?x.
  }
  ''',
  initNs = {"ns": ns, "rdfs": RDFS, "rdf": RDF}
)
for r in g.query(q2):
   print(r.s)
# TO DO
# Visualize the results


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[14]:


for s,p,o in g.triples((None, None, ns.Person)):
  print(s,p,o)

q3 = prepareQuery('''
   SELECT ?s ?p ?o WHERE { 
    ?x rdfs:subClassOf* ns:Person.
    ?s rdf:type ?x.
    ?s ?p ?o
  }
  ''',
  initNs ={"rdfs":RDFS,"ns":ns,"rdf":RDF}
)
for r in g.query(q3):
  print(r)



