import pygal

bar_char = pygal.Bar()
bar_char.x_labels = ['haschild-yes', 'haschild-false', 'gender-male', 'gender-female']
bar_char.add('seed', [0.20, 0.80, 0.3, 0.4, 1, 1])
bar_char.add('magnify', [0.19, 0.81, 0.29, 0.39, 1, 1])
bar_char.render_to_file('test.svg')
# bar_char.render_to_png

array = []
array.append(5)
array.append(6)
print array
