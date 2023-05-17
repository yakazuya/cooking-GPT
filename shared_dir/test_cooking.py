import openai
from api_key import API_KEY,ORGANIZATION_KEY

openai.organization = ORGANIZATION_KEY
openai.api_key = API_KEY

def responce_gpt(food_list):
    
    # ここのなんかかっこいい書き方知りませんか
    if len(food_list) == 1:
        connect_text:str = 'Please tell me the name and process of cooking with ' \
                                + f'{food_list[-1]}'
    else:
        connect_text:str = 'Please tell me the name and process of cooking with ' \
                                + ', '.join(food_list[:len(food_list)-1])  \
                                        + f' and {food_list[-1]}'
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=connect_text,
        max_tokens=2000,
        temperature=0.7,
        n=1,
        stop=None,
    )
    
    return response.choices[0].text

if __name__ == "__main__":
    
    food_list:list = ['potate','tomato','cheese']
    
    text_response = responce_gpt(food_list)
    