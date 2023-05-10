import openai
from api_key import API_KEY,ORGANIZATION_KEY

openai.organization = API_KEY
openai.api_key = ORGANIZATION_KEY

def responce_gpt():
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt='please green pepper cooking',
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )

    print(response.choices[0].text.strip())

    return None

if __name__ == "__main__":
    responce_gpt()
    