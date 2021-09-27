#!/usr/bin/env python
# coding: utf-8

# **Task 06: Modifying RDF(s)**

# In[23]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[18]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")


# Create a new class named Researcher

# In[24]:


ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)


# **TASK 6.1: Create a new class named "University"**
# 

# In[30]:


g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)


# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# In[26]:


tup = (ns.Researcher, RDFS.subClassOf, ns.Person)
g.add(tup)
for s, p, o in g:
  print(s,p,o)


# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

# In[27]:


tupJaneSmith = (ns.JaneSmith, RDF.type, ns.Researcher)
g.add(tupJaneSmith)
for s, p, o in g:
  print(s,p,o)


# **TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

# In[29]:


from rdflib import XSD
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
tupFNJaneSmith = (ns.JaneSmith, VCARD.FN, Literal("Jane Smith", datatype=XSD.string))
tupGiven = (ns.JaneSmith, VCARD.GIVEN, Literal("Jane", datatype=XSD.string))
tupFamily = (ns.JaneSmith, VCARD.Family, Literal("Smith", datatype=XSD.string))

g.add(tupJaneSmith)
g.add(tupGiven)
g.add(tupFamily)

print(g.serialize(format='ttl'))


# **TASK 6.5: Add UPM as the university where John Smith works**

# In[32]:


tupleUPM = (ns.UPM, RDF.type, ns.University)
tupleJohnUPM = (ns.JohnSmith, ns.work, ns.UPM)

g.add(tupleUPM)
g.add(tupleJohnUPM)

print(g.serialize(format='ttl'))

