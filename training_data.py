pos_messages = [('I love this car', 'positive'),
                ('This view is amazing', 'positive'),
                ('I feel great this morning', 'positive'),
                ('I am so excited about the concert', 'positive'),
                ('He is my best friend', 'positive')]

neg_messages = [('I do not like this car', 'negative'),
                ('This view is horrible', 'negative'),
                ('I feel tired this morning', 'negative'),
                ('I am not looking forward to the concert', 'negative'),
                ('He is my enemy', 'negative')]

test_messages = [('I feel happy this morning', 'positive'),
                 ('Larry is my friend', 'positive'),
                 ('I do not like that man', 'negative'),
                 ('My house is not great', 'negative'),
                 ('Your song is annoying', 'negative')]

training_messages = pos_messages + neg_messages
