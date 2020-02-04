from FSA_config import FSA,world_state


def update_world_state(curr_state_dict):
	curr_state = FSA[curr_state_dict['name']]
	if curr_state['effect'] != 0:
		for i in range(len(curr_state['effect'])):
			if curr_state['eff'][i] != '*':
				world_state[i] = curr_state['effect'][i]

def write_memory(curr_input,curr_state_dict):
	curr_state = FSA[curr_state_dict['name']]
	if curr_state['remember'] != 0:
		process_f(curr_state['remember'],args=[curr_input])

def text_to_speech(curr_state_dict):
	curr_state = FSA[curr_state_dict['name']]
	turn = ''
	if curr_state['speak'] != 0:
		if callable(curr_state['speak']):
			turn = process_f(curr_state['speak'],args=[])
		else:
			turn = curr_state['speak']

		print(turn)
	

#TODO
def speak(turn):
	return 0
			

def speech_to_text(curr_state_dict):
	curr_state = FSA[curr_state_dict['name']]
	if curr_state['hear'] != 0:
		return raw_input('Scrivi: ')

#TODO
def hear():
	return 0

def retrieve_successors(curr_input,curr_state_dict):
	curr_state = FSA[curr_state_dict['name']]

	if curr_state['decide'] != 0:
		successors = process_f(curr_state['decide'], args=[curr_input,curr_state['successors'],FSA,world_state])
	else:
		successors = [{'name':curr_state['successors'][0]['name']}]
	return successors

def execute_generic_action(curr_state_dict):
	curr_state = FSA[curr_state_dict['name']]
	if curr_state['execute'] != 0:
		process_f(curr_state['execute'])

def process_f(callback,args=[]):
	return callback(args)


#=====================================================================================


debug = False
debug_frontier = False

frontier = []
curr_state_dict = {'name':'ATTESA'}
frontier.append(curr_state_dict)


def main():

	global frontier

	while True:

		if debug_frontier: print(frontier)
		
		curr_state_dict = frontier.pop(0)

		update_world_state(curr_state_dict)
		if debug: print(''.join(world_state),curr_state_dict['name'])

		text_to_speech(curr_state_dict)

		execute_generic_action(curr_state_dict)

		curr_input = speech_to_text(curr_state_dict)

		successors = retrieve_successors(curr_input,curr_state_dict)

		if 'UNK' not in successors[0]['name']: 
			write_memory(curr_input,curr_state_dict)

		frontier += [s for s in successors if s not in frontier]



main()

