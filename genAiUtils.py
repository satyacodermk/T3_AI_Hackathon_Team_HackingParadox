import openai
from openai import OpenAIError

import cohere



class gptLLM:
    def __init__(self,api_key=None) -> None:
        if api_key==None:
            return "Please provide API Key inorder to use GPT LLM models"
        else:
            openai.api_key=api_key
    
    def generate_response(self,prompt,engine='text_davinci-003',max_tokens=500,temperature=0.5):

        if prompt=="":
            return "Empty input to model"
        else:
            try:
                self.response=openai.Completion.create(
                    engine=engine,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    n=1,
                    stop=None,
                    temperature=temperature
                )

            except OpenAIError as e:
                return f"OpenAI API Error: {e}"
            
            except Exception as e:
                return f"An unexpected error occurred: {e}"


            return self.response.choices[0].text.strip()



class cohereLLM:
    def __init__(self,api_key) -> None:
        if api_key==None:
            return "Please provide API Key inorder to use Cohere LLM models"
        else:
            self.co=cohere.Client(api_key)
    

    def generate_response(self,prompt,engine='command-nightly',max_tokens=500,temperature=0.5):

        if prompt=="":
            return "Empty input to model"
        else:
            try:
                self.response=self.co.generate(
                    model=engine,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    p=0.75,
                    stop=None,
                    temperature=temperature
                )

            except Exception as e:
                return f"An unexpected error occurred: {e}"


            return self.response.generations[0].text.strip()
