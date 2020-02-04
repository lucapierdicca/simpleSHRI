from custom_functions import *
#from graphviz import Digraph

def fsa_viz(file_id,text,annotations):

	f = Digraph('FSA', format='png')

	for k in FSA.keys():
		f.node(k)

	for k,v in FSA.items():
		for s in v['successors']:
			f.edge(k,s['name'])

	f.render(cleanup=True)


robot_memory = []
world_state = ['0','0','0','0','0']


#===============================================================================================================
#=========================================== STATES ============================================================


ATTESA = {'effect':0,
		  'speak':'Chiamami quando sei pronto!',
		  'execute':attesa_exe,
		  'hear':1,
		  'remember':0,
		  'decide':attesa_dec,
		  'successors':[{'name':'SALUTO','in':'Alexa','pre':''},
		  				{'name':'ATTESA_UNK','in':'','pre':''}],
		  'name':'ATTESA'}


ATTESA_UNK = {'effect':0,		  
		  'speak':'Scusa non ho capito, potresti ripetere?',
		  'execute':0,
		  'hear':1,
		  'remember':0,
		  'decide':attesa_dec,
		  'successors':[{'name':'SALUTO','in':'Alexa','pre':''},
		  				{'name':'ATTESA_UNK','in':'','pre':''}],
		  'name':'ATTESA_UNK'}

SALUTO = {'effect':0,
		  'speak':'Ciao, come ti chiami?',
		  'execute':0,
		  'hear':1,
		  'remember':saluto_rem,
		  'decide':0,
		  'successors':[{'name':'RACCOMANDAZIONE','in':'','pre':''}],
		  'name':'SALUTO'}

RACCOMANDAZIONE = {'effect':0,
		  'speak':raccomandazione_spe,
		  'execute':0,
		  'hear':0,
		  'remember':0,
		  'decide':0,
		  'successors':[{'name':'ATTESA','in':'','pre':''}],
		  'name':'RACCOMANDAZIONE'}





FSA = {'ATTESA':ATTESA,
		'ATTESA_UNK':ATTESA_UNK,
	   'RACCOMANDAZIONE':RACCOMANDAZIONE,
	   'SALUTO':SALUTO}


#visualizzazione FSA (richiede PyGraphViz)
#fsa_viz()

