"""
Screen the KEGG database
"""

from Bio import Entrez
from Bio.Entrez import efetch, read
import re
import pprint
import os
from bioservices import *

Entrez.email = 'murlock.raspberypi@gmail.com'


def get_ListOfCommunPathway(elt1, elt2):

	"""
	-> elt1 and elt2 are KEGG id
	return the list of commun pathway between elt1 and elt2
	-> Use bioservices
	-> Internet connection needed
	-> Use KEGG database
	-> "hsa" correspond to human in KEGG database
	"""

	k = KEGG(verbose=False)

	list_OfCommunPathway = []
	list_pathways_elt1 = k.get_pathway_by_gene(str(elt1), "hsa")
	list_pathways_elt2 = k.get_pathway_by_gene(str(elt2), "hsa")

	for pathway_elt1 in list_pathways_elt1.keys():
		for pathway_elt2 in list_pathways_elt2.keys():
			if(str(pathway_elt1) == str(pathway_elt2)):
				list_OfCommunPathway.append(str(pathway_elt1))

	return list_OfCommunPathway




##---------------------------------------------------##
## Exemple d'utilisation des fonctions de l'API KEGG ##
##---------------------------------------------------##
#k = KEGG(verbose=False)
#k.find("hsa", "zap70")
#pathway = k.get_pathway_by_gene("7535", "hsa")
#print pathway
#k.show_pathway("hsa04064", keggid={"7535": "red"})