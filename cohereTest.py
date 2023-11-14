import cohere

co=cohere.Client('LNmCAXeLftUAyjTvFh3dNYD4EJ9NtgLpg8pFaFqw')
response=co.generate(
    model='command-nightly',
    prompt='for cohere, which model is best suitable to do analysis',
    max_tokens=100,
    temperature=0.7,
    k=0,
    p=0.75,
    stop_sequences=[],
    return_likelihoods='NONE'
)

print("Prediction: "+response.generations[0].text)