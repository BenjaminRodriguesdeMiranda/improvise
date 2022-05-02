import random
import math

test_sequence = [('E', 0), ('D', 0.25), ('C', 0.5), ('D', 0.75), ('E', 1), ('E', 1.25), ('E', 1.5), ('D', 2.0),
                 ('D', 2.25), ('D', 2.5), ('E', 3.0), ('G', 3.25), ('G', 3.5), ('E', 4.0), ('D', 4.25), ('C', 4.5),
                 ('D', 4.75), ('E', 5.0), ('E', 5.25), ('E', 5.5), ('E', 5.75), ('D', 6.0), ('D', 6.25), ('E', 6.5),
                 ('D', 6.75), ('C', 7.0)]
number_of_notes = 8
transition_frequencies = [[0 for i in range(number_of_notes)] for j in range(number_of_notes)]
transition_probabilities = [[0 for i in range(number_of_notes)] for j in range(number_of_notes)]

def lowc_to_lowc():
	transition_frequencies[0][0] = transition_frequencies[0][0]+1
def d_to_lowc():
	transition_frequencies[1][0] = transition_frequencies[1][0]+1
def e_to_lowc():
	transition_frequencies[2][0] = transition_frequencies[2][0]+1
def f_to_lowc():
	transition_frequencies[3][0] = transition_frequencies[3][0]+1
def g_to_lowc():
	transition_frequencies[4][0] = transition_frequencies[4][0]+1
def a_to_lowc():
	transition_frequencies[5][0] = transition_frequencies[5][0]+1
def b_to_lowc():
	transition_frequencies[6][0] = transition_frequencies[6][0]+1
def highc_to_lowc():
	transition_frequencies[7][0] = transition_frequencies[7][0]+1
def lowc_to_d():
	transition_frequencies[0][1] = transition_frequencies[0][1]+1
def d_to_d():
	transition_frequencies[1][1] = transition_frequencies[1][1]+1
def e_to_d():
	transition_frequencies[2][1] = transition_frequencies[2][1]+1
def f_to_d():
	transition_frequencies[3][1] = transition_frequencies[3][1]+1
def g_to_d():
	transition_frequencies[4][1] = transition_frequencies[4][1]+1
def a_to_d():
	transition_frequencies[5][1] = transition_frequencies[5][1]+1
def b_to_d():
	transition_frequencies[6][1] = transition_frequencies[6][1]+1
def highc_to_d():
	transition_frequencies[7][1] = transition_frequencies[7][1]+1
def lowc_to_e():
	transition_frequencies[0][2] = transition_frequencies[0][2]+1
def d_to_e():
	transition_frequencies[1][2] = transition_frequencies[1][2]+1
def e_to_e():
	transition_frequencies[2][2] = transition_frequencies[2][2]+1
def f_to_e():
	transition_frequencies[3][2] = transition_frequencies[3][2]+1
def g_to_e():
	transition_frequencies[4][2] = transition_frequencies[4][2]+1
def a_to_e():
	transition_frequencies[5][2] = transition_frequencies[5][2]+1
def b_to_e():
	transition_frequencies[6][2] = transition_frequencies[6][2]+1
def highc_to_e():
	transition_frequencies[7][2] = transition_frequencies[7][2]+1
def lowc_to_f():
	transition_frequencies[0][3] = transition_frequencies[0][3]+1
def d_to_f():
	transition_frequencies[1][3] = transition_frequencies[1][3]+1
def e_to_f():
	transition_frequencies[2][3] = transition_frequencies[2][3]+1
def f_to_f():
	transition_frequencies[3][3] = transition_frequencies[3][3]+1
def g_to_f():
	transition_frequencies[4][3] = transition_frequencies[4][3]+1
def a_to_f():
	transition_frequencies[5][3] = transition_frequencies[5][3]+1
def b_to_f():
	transition_frequencies[6][3] = transition_frequencies[6][3]+1
def highc_to_f():
	transition_frequencies[7][3] = transition_frequencies[7][3]+1
def lowc_to_g():
	transition_frequencies[0][4] = transition_frequencies[0][4]+1
def d_to_g():
	transition_frequencies[1][4] = transition_frequencies[1][4]+1
def e_to_g():
	transition_frequencies[2][4] = transition_frequencies[2][4]+1
def f_to_g():
	transition_frequencies[3][4] = transition_frequencies[3][4]+1 
def g_to_g():
	transition_frequencies[4][4] = transition_frequencies[4][4]+1
def a_to_g():
	transition_frequencies[5][4] = transition_frequencies[5][4]+1
def b_to_g():
	transition_frequencies[6][4] = transition_frequencies[6][4]+1
def highc_to_g():
	transition_frequencies[7][4] = transition_frequencies[7][4]+1
def lowc_to_a():
	transition_frequencies[0][5] = transition_frequencies[0][5]+1
def d_to_a():
	transition_frequencies[1][5] = transition_frequencies[1][5]+1
def e_to_a():
	transition_frequencies[2][5] = transition_frequencies[2][5]+1
def f_to_a():
	transition_frequencies[3][5] = transition_frequencies[3][5]+1
def g_to_a():
	transition_frequencies[4][5] = transition_frequencies[4][5]+1
def a_to_a():
	transition_frequencies[5][5] = transition_frequencies[5][5]+1
def b_to_a():
	transition_frequencies[6][5] = transition_frequencies[6][5]+1
def highc_to_a():
	transition_frequencies[7][5] = transition_frequencies[7][5]+1
def lowc_to_b():
	transition_frequencies[0][6] = transition_frequencies[0][6]+1
def d_to_b():
	transition_frequencies[1][6] = transition_frequencies[1][6]+1
def e_to_b():
	transition_frequencies[2][6] = transition_frequencies[2][6]+1
def f_to_b():
	transition_frequencies[3][6] = transition_frequencies[3][6]+1
def g_to_b():
	transition_frequencies[4][6] = transition_frequencies[4][6]+1
def a_to_b():
	transition_frequencies[5][6] = transition_frequencies[5][6]+1
def b_to_b():
	transition_frequencies[6][6] = transition_frequencies[6][6]+1
def highc_to_b():
	transition_frequencies[7][6] = transition_frequencies[7][6]+1
def lowc_to_highc():
	transition_frequencies[0][7] = transition_frequencies[0][7]+1
def d_to_highc():
	transition_frequencies[1][7] = transition_frequencies[1][7]+1
def e_to_highc():
	transition_frequencies[2][7] = transition_frequencies[2][7]+1
def f_to_highc():
	transition_frequencies[3][7] = transition_frequencies[3][7]+1
def g_to_highc():
	transition_frequencies[4][7] = transition_frequencies[4][7]+1
def a_to_highc():
	transition_frequencies[5][7] = transition_frequencies[5][7]+1
def b_to_highc():
	transition_frequencies[6][7] = transition_frequencies[6][7]+1
def highc_to_highc():
	transition_frequencies[7][7] = transition_frequencies[7][7]+1

index_dictionary = {'C': lambda x: 0, 'D': lambda x: 1, 'E': lambda x: 2, 'F': lambda x: 3, 'G': lambda x: 4, 'A': lambda x: 5, 'B': lambda x: 6, 'C': lambda x: 7}

key_dictionary = {'C': {'C': lowc_to_lowc, 'D': d_to_lowc, 'E': e_to_lowc, 'E': f_to_lowc, 'G': g_to_lowc, 'A': a_to_lowc, 'B': b_to_lowc, 'C': highc_to_lowc},
                  'D': {'C': lowc_to_d, 'D': d_to_d, 'E': e_to_d, 'F': f_to_d, 'G': g_to_d, 'A': a_to_d, 'B': b_to_d, 'C': highc_to_d},
                  'E': {'C': lowc_to_e, 'D': d_to_e, 'E': e_to_e, 'F': f_to_e, 'G': g_to_e, 'A': a_to_e, 'B': b_to_e, 'C': highc_to_e},
                  'F': {'C': lowc_to_f, 'D': d_to_f, 'E': e_to_f, 'F': f_to_f, 'G': g_to_f, 'A': a_to_f, 'B': b_to_f, 'C': highc_to_f},
                  'G': {'C': lowc_to_g, 'D': d_to_g, 'E': e_to_g, 'F': f_to_g, 'G': g_to_g, 'A': a_to_g, 'B': b_to_g, 'C': highc_to_g},
                  'A': {'C': lowc_to_a, 'D': d_to_a, 'E': e_to_a, 'F': f_to_a, 'G': g_to_a, 'A': a_to_a, 'B': b_to_a, 'C': highc_to_a},
                  'B': {'C': lowc_to_b, 'D': d_to_b, 'E': e_to_b, 'F': f_to_b, 'G': g_to_b, 'A': a_to_b, 'B': b_to_b, 'C': highc_to_b},
                  'C': {'C': lowc_to_highc, 'D': d_to_highc, 'E': e_to_highc, 'F': f_to_highc, 'G': g_to_highc, 'A': a_to_highc, 'B': b_to_highc, 'C': highc_to_highc}}

def create_transition_matrix(sequence):
	for i in range(len(sequence)-1):
		key_dictionary[sequence[i][0]][sequence[i+1][0]]()
	column_totals = [0 for i in range(number_of_notes)]
	for i in range(len(transition_frequencies)):
		total = 0
		for j in range(len(transition_frequencies[i])):
			total = total+transition_frequencies[j][i]
		column_totals[i] = total
	for i in range(number_of_notes):
		column_total = column_totals[i]
		for j in range(number_of_notes):
			transition_probabilities[i][j] = (transition_frequencies[j][i]+1)/(column_total+number_of_notes)

def generate_note(previous_note):
	index = index_dictionary[previous_note](None)
	rand = random.random()
	probability_counter = transition_probabilities[index][0]
	if rand < probability_counter:
		return 'C'
	probability_counter = probability_counter+transition_probabilities[index][1]
	if rand < probability_counter:
		return 'D'
	probability_counter = probability_counter+transition_probabilities[index][2]
	if rand < probability_counter:
		return 'E'
	probability_counter = probability_counter+transition_probabilities[index][3]
	if rand < probability_counter:
		return 'F'
	probability_counter = probability_counter+transition_probabilities[index][4]
	if rand < probability_counter:
		return 'G'
	probability_counter = probability_counter+transition_probabilities[index][5]
	if rand < probability_counter:
		return 'A'
	probability_counter = probability_counter+transition_probabilities[index][6]
	if rand < probability_counter:
		return 'B'
	else:
		return 'C'

def find_shortest_interval(note_info):
	array_length = len(note_info)
	i = 0
	minimum = 99
	while i < array_length-1:
		current_interval = note_info[i+1][1]-note_info[i][1]
		if current_interval < minimum:
			minimum = current_interval
		i += 1
	return round(minimum, 5)

def find_longest_interval(note_info):
	array_length = len(note_info)
	i = 0
	maximum = 0
	while i < array_length-1:
		current_interval = note_info[i+1][1]-note_info[i][1]
		if current_interval > maximum:
			maximum = current_interval
		i += 1
	return round(maximum, 5)

def align_notes(note_info_tuples, interval):
	note_info = []
	for i in range(len(note_info_tuples)):
		temp_tuple = note_info_tuples[i]
		temp_list = list(temp_tuple)
		note_info.append(temp_list)
	num_time_stamps = math.ceil(note_info[len(note_info[0])-1][1]/interval)
	time_stamps = [0]*(num_time_stamps+1)
	i = 1
	while i < len(time_stamps):
		time_stamps[i] = round((i)*interval, 5)
		i = i + 1
	i = 0
	while i < len(note_info[1]):
		closest = 999
		current_best_timing = note_info[i][1]
		j = 0
		while j < len(time_stamps):
			if abs(note_info[i][1]-time_stamps[j]) < closest:
				closest = abs(note_info[i][1]-time_stamps[j])
				current_best_timing = time_stamps[j]
			j = j+1
		note_info[i][1] = current_best_timing
		i = i+1
	formatted_note_info = []
	for i in range(len(note_info)):
		temp_list = note_info[i]
		temp_tuple = tuple(temp_list)
		formatted_note_info.append(temp_tuple)
	return formatted_note_info

def generate_timings(sequence):
	aligned_sequence = align_notes(sequence, find_shortest_interval(sequence))
	shortest_interval = find_shortest_interval(aligned_sequence)
	longest_interval = find_longest_interval(aligned_sequence)
	number_of_timings = int(longest_interval/shortest_interval)
	time_values = [0 for i in range(number_of_timings)]
	time_frequencies = [0 for i in range(number_of_timings)]
	time_values[0] = shortest_interval
	time_values[len(time_values)-1] = longest_interval
	i = 1
	while i < number_of_timings-1:
		time_values[i] = time_values[i-1]+shortest_interval
		i = i+1
	for j in range(len(aligned_sequence)-1):
		for k in range(len(time_values)):
			if ((aligned_sequence[j+1][1]-aligned_sequence[j][1] >= time_values[k]-(shortest_interval/2)) & 
                            (aligned_sequence[j+1][1]-aligned_sequence[j][1] <= time_values[k]+(shortest_interval/2))):
				time_frequencies[k] = time_frequencies[k]+1
	raw_probabilities = [0 for j in range(len(time_frequencies))]
	ptotal = 0
	for j in time_frequencies:
		ptotal = ptotal+j
	for j in range(len(raw_probabilities)):
		raw_probabilities[j] = time_frequencies[j]/ptotal
	return raw_probabilities, time_values

def generate_interval(timings):
	rand = random.random()
	probability_counter = timings[0][0]
	for i in range(len(timings)):
		if rand < probability_counter:
			return timings[1][i]
		if i < len(timings)-1:
			probability_counter = probability_counter+timings[1][i+1]

def improvise(note, improvisation_length, timings):
	improvised_notes = []
	current_time = generate_interval(timings)
	improvised_notes.append((generate_note(note), current_time))
	for i in range(improvisation_length-1):
		current_time = current_time+generate_interval(timings)
		improvised_notes.append((generate_note(improvised_notes[i][0]), current_time))
	return improvised_notes

def create_music(sequence, improvisation_length):
	create_transition_matrix(sequence)
	improvised_sequence = improvise(sequence[len(sequence)-1][0], improvisation_length, generate_timings(sequence))
	print(improvised_sequence)
	return improvised_sequence

create_music(test_sequence, 20)