sequence = []
longest_sequence_len = 0
longest_sequence_starter = 0
i = 13
while i < 1000000:
	j = i
	sequence.append(i)
	while j != 1:
		if j % 2 == 0:
			j = j/2
			sequence.append(j)
		else:
			j = (j * 3) + 1
			sequence.append(j)
	if len(sequence) > longest_sequence_len:
		longest_sequence_len = len(sequence)
		longest_sequence_starter = sequence[0]
	
	sequence = []

	i += 1

print longest_sequence_starter
