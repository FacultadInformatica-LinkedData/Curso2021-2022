#!/usr/bin/env python
# coding: utf-8

# **Task 06: Modifying RDF(s)**

# In[4]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[5]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")


# Create a new class named Researcher

# In[9]:


ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)


# **TASK 6.1: Create a new class named "University"**
# 

# In[8]:


ns = Namespace("http://somewhere#")
g.add((ns.University, RDF.type, RDFS.Class))
# TO DO
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# In[13]:


g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

# TO DO
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

# In[14]:


fullName = Literal("John Smith")
EX = Namespace("http://somewhere#")
johnURI = EX.JohnSmith
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
resource = (johnURI, VCARD.FN, fullName)
g.add(resource)
# TO DO
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

# In[15]:


g.add((EX.JaneSmith, VCARD.FN, Literal("Jane Smith")))
g.add((EX.JaneSmith, VCARD.Faimily, Literal("Smith")))
# TO DO
# Visualize the results


# **TASK 6.5: Add UPM as the university where John Smith works**

# In[16]:



g.add((EX.JaneSimith, ns.work,ns.University ))
# TO DO
# Visualize the results


# In[ ]:




