import pygal

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
# print(results)
results = [die.roll() for roll_num in range(1000)]

# Analyze the results.
# frequencies = []
# for value in die.values():
#     frequency = results.count(value)
#     frequencies.append(frequency)
# print(frequencies)
frequencies = [results.count(value) for value in die.values()]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = die.values()  # TODO: 排序
# hist.x_labels = [str(x) for x in die.values()]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('output/die_visual.svg')
