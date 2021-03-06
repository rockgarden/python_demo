import pygal

from die import Die

# Create two D6 dice.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
# results = []
# for roll_num in range(2000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(5000)]

# Analyze the results.
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = range(2, max_result + 1)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('output/die_2_visual.svg')
