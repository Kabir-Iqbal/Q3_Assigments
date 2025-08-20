# from turtle import title
# from agents import Agent, Runner, function_tool
# from connection import config
# import requests
# import re


# # function tool
# @function_tool
# def search_products(keyword: str)->str:
#     try:
#         url = 'https://hackathon-apis.vercel.app/api/products'
#         response = requests.get(url)
#         response.raise_for_status()
#         products = response.json()

#         words = re.findall(r"\b\w+\b", keyword.lower())
#         stopwords = {"the", 'with', 'under', 'above', 'for', 'of', 'and', 'for', 'of', 'and', 'below', 'or', 'a', 'an','in','to','between','is','best'}
#         keywords = [w for w in words if w not in stopwords]


#         filtered = []
#         for p in products:
#             title = p.get('title', '').lower()
#             price = p.get('price',None)
#             if not title or price is None:
#                 continue
#             if any(kw in title for kw in keywords):
#                 filtered.append(f'- {p['title']} | Rs {price}')
        
#         if filtered:
#             return '\n' .json(filtered[:5])
#         else:
#             return ''
#     except Exception as e:
#         return f' Api Error: {str(e)}'


# def main():
#     print('Welcome to the shopping agent')
#     user_question = input('What product are you looking for ?')

#     agent = Agent(
#     name = 'Product research',
#     instructions='You are helpful shopping assistant that answers product related question and recommands relevant products.',
#     tools=[search_products]
#     )

#     result = Runner.run_sync(agent, user_question, run_config=config)
#     result.final_output


#     # # product_results = search_products(user_question)
#     # product_results = search_products(user_question)


#     if result:
#         print('\n Matching Products: \n', result.final_output)
#         print('\n Agent Answer:\n', result.final_output)


# if __name__ == "__main__":
#     main()







from agents import Agent, Runner, function_tool
from connection import config
import requests
import re

@function_tool
def search_products(keyword: str) -> str:
    try:
        url = 'https://hackathon-apis.vercel.app/api/products'
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()

        
        # print("Total products fetched:", len(products))  # 👈 یہ لائن add کرو
        # print("Sample product:", products[0])  # 👈 یہ بھی add کرو (صرف debug کیلئے)

        words = re.findall(r"\b\w+\b", keyword.lower())
        stopwords = {"the", 'with', 'under', 'above', 'for', 'of', 'and', 'below', 'or', 'a', 'an','in','to','between','is','best'}
        keywords = [w for w in words if w not in stopwords]

        filtered = []
        for p in products:
            name = p.get('name', '').lower()
            price = p.get('price', None)
            if not name or price is None:
                continue
            if any(kw in name for kw in keywords):
                filtered.append(f"- {p['name']} | Rs {price}")
        
        if filtered:
            return '\n'.join(filtered[:5])
        else:
            return 'I am sorry, I cannot find any matching products.'
    except Exception as e:
        return f'API Error: {str(e)}'


def main():
    print('Welcome to the shopping agent')
    user_question = input('What product are you looking for? ')

    agent = Agent(
        name='Product research',
        instructions='You are a helpful shopping assistant that answers product related questions and recommends relevant products.',
        tools=[search_products]
    )

    result = Runner.run_sync(agent, user_question, run_config=config)

    if result:
        print('\n Matching Products:\n', result.final_output)
        print('\n Agent Answer:\n', result.final_output)


if __name__ == "__main__":
    main()
