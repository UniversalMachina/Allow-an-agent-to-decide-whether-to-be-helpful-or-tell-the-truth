#https://github.com/webaverse-studios/webaverse/issues/113
#fixes issue 113

import random



class Personality:
    def __init__(self, name, untruthful_prob, truthful_prob):
        self.name = name
        self.untruthful_prob = untruthful_prob
        self.truthful_prob = truthful_prob

# Define valid personalities with their respective probabilities for being untruthful or truthful
personalities = [
    Personality('Friendly', 0.2, 0.8),
    Personality('Honest', 0.1, 0.9),
    Personality('Neutral', 0.5, 0.5),
    Personality('Sarcastic', 0.9, 0.1),
    Personality('Indifferent', 0.7, 0.3),
]

def select_personality(personalities):
    return random.choice(personalities)

def agent_decision(question, untruthful_response, truthful_response, personality):
    decision = random.choices(
        ['untruthful', 'truthful'],
        weights=[personality.untruthful_prob, personality.truthful_prob]
    )[0]

    if decision == 'untruthful':
        return f"Untruthful response: {untruthful_response}"
    else:
        return f"Truthful response: {truthful_response}"

# Example usage
question = "What is the weather like today?"
untruthful_response = "This is a lie"
truthful_response = "This is the truth."

personality = select_personality(personalities)
print(f"Agent's personality: {personality.name}")
response = agent_decision(question, untruthful_response, truthful_response, personality)
print(response)
