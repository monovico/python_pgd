from GPTJ.Basic_api import SimpleCompletion

prompt = 'where is illinois'

max_length = 100
temperature = 0.09
top_probability = 1.0
query = SimpleCompletion(prompt, length=max_length, t=temperature, top=top_probability)
query.simple_completion()
Query = query.simple_completion()

print(Query)
