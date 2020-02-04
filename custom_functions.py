import FSA_config 

def state_entails(action,state):
	if action['pre'] != '':
		for i,j in zip(action['pre'],state):
			if i != j and i != '*':
				return False
	return True

#===========================================================================
#===========================================================================

def attesa_dec(args):
	curr_input = args[0]
	successors = args[1]
	FSA = args[2]
	world_state = args[3]

	applicable_successors = []
	for s in successors:
		if state_entails(s,world_state):
			#NLU condition
			if curr_input in s['in']:
				applicable_successors.append({'name':s['name'],
											  'input':curr_input})
	
	if len(applicable_successors) == 0:
		applicable_successors.append({'name':successors[-1]['name']})

	return applicable_successors

def attesa_exe(args):
	del FSA_config.robot_memory[:]

def saluto_rem(args):
	curr_input = args[0]

	#NLU condition
	tokens = curr_input.split()
	user_name = tokens[-1]

	FSA_config.robot_memory.append({'user_name':user_name})

def raccomandazione_spe(args):
	user_name = FSA_config.robot_memory[0]['user_name']
	turn = user_name+' lavati le mani e non parlare coi cinesi! Addio!'

	return turn
