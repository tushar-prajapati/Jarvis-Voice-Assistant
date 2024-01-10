fileopen = open("Data\\api.txt", "r")
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def questions_replier(question, chat_log = None):
    Filelog = open("Database\qna_log.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()
    
    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f"{chat_log}Question : {question}\nJarvis : "
    response = completion.create(model = "text-davinci-002",
    temperature = 0,
    prompt = prompt,
    max_tokens = 100,
    top_p = 1,
    frequency_penalty = .5,
    presence_penalty = 0)
    
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    Filelog = open("Database\qna_log.txt", "w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer
