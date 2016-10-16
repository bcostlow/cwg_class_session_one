# dicts can take an iterable of pairs as a constructor

demo_dict_one = dict([('size', 'large'), ('color', 'blue')])
print(demo_dict_one)

# for small dicts created inline, this syntax is clearer

demo_dict_two = {'color': 'red', 'size': 'medium'}
print(demo_dict_two)

# but if you already have your keys and values as sequences
fields = ['size', 'color', 'material']
order = ['small', 'pink', 'cotton']

demo_dict_three = dict(zip(fields, order))
print(demo_dict_three)
