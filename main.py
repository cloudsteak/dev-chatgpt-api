import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# response = get_completion("What is the capital of France?")
# response = get_completion(
#     """Take the letters in \
# l-o-l-l-i-p-o-p and reverse them"""
# )
# print(response)


def get_completion_from_messages(
    messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
        max_tokens=max_tokens,  # the maximum number of tokens the model can ouptut
    )
    return response.choices[0].message["content"]


# messages = [
#     {
#         "role": "system",
#         "content": """You are an assistant who\
#  responds in the style of Dr Seuss.""",
#     },
#     {
#         "role": "user",
#         "content": """write me a very short poem\
#  about a happy carrot""",
#     },
#     {
#         "role": "user",
#         "content": """Tell me a joke""",
#     },
# ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)


# messages = [
#     {
#         "role": "system",
#         "content": """You are a student""",
#     },
#     {
#         "role": "user",
#         "content": """Tell me a joke""",
#     },
# ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)


# length
# messages =  [
# {'role':'system',
#  'content':'All your responses must be \
# one sentence long.'},
# {'role':'user',
#  'content':'write me a story about a happy carrot'},
# ]
# response = get_completion_from_messages(messages, temperature =1)
# print(response)


# combined
# messages =  [
# {'role':'system',
#  'content':"""You are an assistant who \
# responds in the style of Dr Seuss. \
# All your responses must be one sentence long."""},
# {'role':'user',
#  'content':"""write me a story about a happy carrot"""},
# ]
# response = get_completion_from_messages(messages,
#                                         temperature =1)
# print(response)


def get_completion_and_token_count(
    messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message["content"]

    token_dict = {
        "prompt_tokens": response["usage"]["prompt_tokens"],
        "completion_tokens": response["usage"]["completion_tokens"],
        "total_tokens": response["usage"]["total_tokens"],
    }

    return content, token_dict


messages = [
    {
        "role": "system",
        "content": """Egyetemsita vagy, aki\
 sok szlenget használ""",
    },
    {
        "role": "user",
        "content": """mondj egy viccet""",
    },
]
response, token_dict = get_completion_and_token_count(messages)
print(response)
print(token_dict)