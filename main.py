# Importing random module
import random

# Defining list of phrases which will help to build a story

Sentence_starter = ['About 150 years ago', ' In the 10 EC', 'Once upon a time']
character = [' there lived a king.',' there was a woman named Alexia.',
			' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a day-out to ']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 30s', ' who seemed very young and feeble']
work = [' searching something.', ' digging a well on roadside by a marketplace.']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))
