import os
from dotenv import load_dotenv
from colorama import Fore, Back, Style
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model_name="text-davinci-003")

template = "{this}"
prompt = PromptTemplate(template=template, input_variables=["this"])
chain = LLMChain(llm=llm, prompt=prompt)

print('Type something and press Enter to ask, type "q" to quit: ')
print()

while True:
    print(Style.RESET_ALL + "User question:" + Style.RESET_ALL)
    typing = input()
    if typing == "q":
        break
    else:
        print(
            "Bot answer:"
            + Fore.WHITE
            + Back.RED
            + chain.run({"this": typing})
            + Style.RESET_ALL
        )
