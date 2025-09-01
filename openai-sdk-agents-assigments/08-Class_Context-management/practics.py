# # import asyncio
# # from agents import (
# #     Agent,
# #     GuardrailFunctionOutput, 
# #     InputGuardrailTripwireTriggered, 
# #     Runner,
# #     input_guardrail,
# #     trace
# #     )
# # from connection import config
# # from pydantic import BaseModel

# ########################### Input Guardial ###########################

# # class medicine_output(BaseModel):
# #     response : str
# #     isExceedquery : bool
    

# # medicine_agent = Agent(
# #     name = 'Medicine_Agent',
# #     instructions= 'You are Medicine agent only reply medicine query',
# #     output_type=medicine_output
# # )


# # @input_guardrail
# # async def medicine_Query_checker(ctx, agent, input):
# #     result = await Runner.run(
# #         medicine_agent,
# #         input,
# #         run_config=config
# #     )

# #     print(result.final_output)

# #     return GuardrailFunctionOutput(
# #         output_info=result.final_output.response,
# #         tripwire_triggered=result.final_output.isExceedquery
# #     )



# # # main agent
# # worker = Agent(
# #     name = 'Worker agent',
# #     instructions= 'You are worker agent if you get any query from user you should ask medicine agent',
# #     input_guardrails=[medicine_Query_checker]
# # )



# # async def main():
# #     try:
# #         Result = await Runner.run(worker, 'Whats Carola car price in pakistan?', run_config=config)
# #         print(Result.final_output)
# #     except InputGuardrailTripwireTriggered:
# #         print('I can  answer medical query only')



# # if __name__== '__main__':
# #     asyncio.run(main())







# # ########################### Ouput Guardial ###########################

# # from agents import (
# #     Agent,
# #     OutputGuardrailTripwireTriggered,
# #     GuardrailFunctionOutput, 
# #     Runner,
# #     output_guardrail, 
# #     trace
# #     )

# # from connection import config
# # from pydantic import BaseModel
# # import rich
# # import asyncio

# # from dotenv import load_dotenv

# # load_dotenv()

# # ######################## Output Guardrail ######################## 
# # # Output validation model for financial advice
# # class Country_City_info(BaseModel):
# #     response: str
# #     isValidCity: bool
# #     isSindhCityOnly: bool
# #     reason: str


# # city_guardrail_agent = Agent(
# #     name='City Information Output Guardrail Agent',
# #     instructions=""" 
# #     You are an output guardrail agent for Pakistani cities (Sindh province only).
# #     Validation rules:
# #     1. If the user asks about the famous city of Pakistan → The correct answer is "Karachi".
# #     2. Only allow city names that belong to Sindh province (e.g., Karachi, Hyderabad, Sukkur, Larkana, Mirpur Khas).
# #     3. If response contains cities outside Sindh, mark it as inappropriate.
# #     """,
# #     output_type=Country_City_info
# # )



# # @output_guardrail
# # async def City_Check_output_guardrail(ctx, agent, output) -> GuardrailFunctionOutput:
# #     """Output guardrail to validate financial advice responses"""
# #     result = await Runner.run(
# #         city_guardrail_agent, 
# #         f"Answer the  response: {output}", 
# #         run_config=config
# #     )
    
# #     return GuardrailFunctionOutput(
# #         output_info=result.final_output.response,
# #         tripwire_triggered= not (
# #             result.final_output.isValidCity and 
# #             result.final_output.isSindhCityOnly
# #         )
# #     )


# # # Main financial advisor agent
# # Pakistani_Cities = Agent(
# #     name="Pakistani Cities Agent",
# #     instructions=""" 
# #     You are an expert on Pakistani cities.
# #     - Only provide information about cities in Pakistan.
# #     - If asked about the famous city of Pakistan, always say "Karachi".
# #     - Keep responses short, clear, and fact-based.
# #     """,
# #     output_guardrails=[City_Check_output_guardrail]
# # )


# # # Triage agent that delegates to financial advisor
# # triage_agent = Agent(
# #     name="Info Triage Agent",
# #     instructions=""" 
# #     You are a triage agent for city-related queries. 
# #     - If the query is about Pakistani cities, delegate it to the Pakistani Cities Agent.
# #     - If the query is unrelated to cities, do not attempt to answer.
# #     """,
# #     handoffs=[Pakistani_Cities],
# # )

# # async def main():
# #     prompt1 = """ which is city of lights city in pakistan ? """ # True
   

# #     try:
# #         result = await Runner.run(
# #             triage_agent, 
# #             prompt1,
# #             run_config=config
# #         )
# #         print("Response passed guardrails:")
# #         print(result.final_output)
# #         # print(result.last_agent)
        
# #     except OutputGuardrailTripwireTriggered as e:
# #         print('Output guardrail triggered - response did not meet safety standards')
        
# # if __name__ == "__main__":
# #     asyncio.run(main())


# ########################### Context Management ###########################

# # import asyncio
# # from connection import config
# # from agents import Agent, RunContextWrapper, Runner, function_tool
# # from pydantic import BaseModel
# # import rich

# # class UserInfo(BaseModel):
# #     user_id: int | str
# #     name: str
# # user = UserInfo(user_id= 1312321, name="Ali Jawwad")

# # @function_tool
# # def get_user_info(wrapper: RunContextWrapper[UserInfo]):
# #     return f'The user info is {wrapper.context}'

# # personal_agent = Agent(
# #     name = "Agent",
# #     instructions="You are a helpful assistant, always call the tool to get user's information",
# #     tools=[get_user_info]
# # )

# # async def main():
# #     result = await Runner.run(
# #         personal_agent, 
# #         # 'What is the user id', 
# #         'What is my name and also tell me my user id', 
# #         run_config=config,
# #         context = user #Local context
# #         )
# #     rich.print(result.final_output)


# # if __name__ == "__main__":
# #     asyncio.run(main())


# import asyncio
# from connection import config
# from agents import Agent, Runner, function_tool,  RunContextWrapper
# from pydantic import BaseModel
# import rich

# class UserInfo(BaseModel):
#     name: str
#     userId: int | str


# user = UserInfo(name= 'Kabir Iqbal', userId=902345689)

# @function_tool
# def get_user_info(wrapper:RunContextWrapper[UserInfo]):
#     return f'the user info is {wrapper.context}'


# assistant = Agent(
#     name='Helpful Assistant',
#     instructions='''You are a helpful assistant, always call the tool to get user's information''',
#     tools=[get_user_info]

# )


# async def main():
#     try:
#         result = await Runner.run(
#             assistant,
#             'What is my name and also tell me my user id',
#             run_config=config,
#             context= user       # context management
#         )
#         print(result.final_output)
#     except :
#         print("Invaild Query")



# if __name__=='__main__':
#     asyncio.run(main())