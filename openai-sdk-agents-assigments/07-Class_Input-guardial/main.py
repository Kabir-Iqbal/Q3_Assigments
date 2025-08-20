from openai.types.responses import response
import rich
import asyncio
from connection import config
from pydantic import BaseModel
from agents import (Agent, OutputGuardrailTripwireTriggered, Runner, 
    input_guardrail,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered, output_guardrail)




# ##################### Home-1  ####################### #

# Exercise # 1 Objective: Make a agent and make an input guardrail trigger. Prompt: I want to change my class timings 
# 😭😭 Outcome: After running the above prompt an InputGuardRailTripwireTriggered in except should be called. See the outcome in LOGS

class student_Output(BaseModel):
    response: str
    isStudentExceed : bool


mannagement_agent = Agent(
    name= 'Mangement Team',
    instructions='''
    Your task is mangement to query of student but slot time will same
     its not be changed in any situation ''',
    
    output_type=student_Output

)


@input_guardrail()
async def security_checker(ctx,agent,input):
    result = await Runner.run(
        mannagement_agent,
        input ,
        run_config=config
    )

    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered= result.final_output.isStudentExceed
    )


# main agent
Student = Agent(
    name= 'Student_Agent',
    instructions='You are student agent you can asky your query to mangement',
    input_guardrails=[security_checker]
)


async def main():
    try:
       result = await Runner.run(Student, 'Hello Mangement Team Can i change my time slot ?', run_config=config)
       print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print('Time Slot will not be change.')



if __name__ == '__main__':
    asyncio.run(main())




##################### Home-2  ####################### #

# Exercise # 2 Objective: Make a father agent and father guardrail. The father stopping his child to run below 26C.


# Stuructured Output
class Father_Output(BaseModel):
    response: str
    isFatherExceed:bool

Father_agent = Agent(
    name = 'Father_Agnet',
    instructions='You are Father agent and you task is to stopping children to run below 26C. Ac ',
    output_type=Father_Output
)

@input_guardrail
async def Father_Permision(ctx,agent,input):
    result = await Runner.run(Father_agent, input, run_config=config)
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isFatherExceed
    )


children = Agent(
    name = 'Children agent',
    instructions='You are children agent you work is only get permission from father',
    input_guardrails=[Father_Permision]
)


async def main():
    try:
       result = await Runner.run(children, "Hello, Dad Can i do 27C on Ac", run_config=config)
       print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print('No You Cant do above from 26C')
   

if __name__ == '__main__':
    asyncio.run(main())






##################### Home-3  ####################### #
# Exercise # 3 Objective: Make a gate keeper agent and gate keeper guardrail. The gate keeper stopping students of other school.

#  Stuructured Output
class Get_Keeper_Output(BaseModel):
    response: str
    isGetkeeperExceed:bool

getKeeper_agent = Agent(
    name = 'GetKeeper_Agnet',
    instructions='You are GetKeeper agent and you task is to stopping other school students to enter in our oxford school ',
    output_type=Get_Keeper_Output
)

@input_guardrail
async def GetKeeper_Permision(ctx,agent,input):
    result = await Runner.run(getKeeper_agent, input, run_config=config)
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isGetkeeperExceed
    )


Student = Agent(
    name = 'Children agent',
    instructions='You are Student agent you task is go other school and get permission ffrom get keeper.',
    input_guardrails=[GetKeeper_Permision]
)


async def main():
    try:
       result = await Runner.run(Student, "Hello, Can I enter in you school Iam student of Bhattai School", run_config=config)
       print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print('No You Cant come, because we cant allow other schools students')
   

if __name__ == '__main__':
    asyncio.run(main())




































# class PassengerOutput(BaseModel):          # structured output .  mean obj or dic
#     response: str
#     isWeightExceed: bool
     
# airport_security_guard = Agent(
#     name = "Airport Security Guard",
#     instructions= """ 
#         Your task is to check the passenger luggage.
#         If passenger's luggage is more then 25KGs, gracefully stop them
#     """,
#      output_type = PassengerOutput
# )


# @input_guardrail
# async def security_guardrail(ctx, agent, input):
#     result = await Runner.run(airport_security_guard, 
#                               input, 
#                               run_config=config
#                               )
#     rich.print(result.final_output)

#     return GuardrailFunctionOutput(
#         output_info= result.final_output.response,
#         tripwire_triggered= True
#     )

# # Main agent
# passenger_agent = Agent(
#     name = 'Passenger',
#     instructions="You are a passenger agent",
#     input_guardrails=[security_guardrail]
# )

# async def main():
#         try:
#             result = await Runner.run(passenger_agent , 'My luggage weight is 20kgs', run_config=config)
#             print("Passenger is onboarded")

#         except InputGuardrailTripwireTriggered:
#              print('Passenger cannot check-in')




        

# if __name__ == "__main__":
#     # asyncio.run(og_main())
#     asyncio.run(main())




####################### Output Guardrails ########################

# class MessageOutput(BaseModel): # Model for Agent Output Type
#     response: str

# class PHDOutput(BaseModel): # Model to trigger the guardrail
#     isPHDLevelResponse: bool

# phd_guardrail_agent = Agent(
#     name = "PHD Guardrail Agent",
#     instructions="""
#         You are a PHD Guardrail Agent that evaluates if text is too complex for 8th grade students. If the response if 
#         very hard to read for an eight grade student deny the agent response
#     """,
#     output_type=PHDOutput
# )

# @output_guardrail
# async def PHD_guardrail(ctx, agent: Agent, output) -> GuardrailFunctionOutput:

#     result = await Runner.run(phd_guardrail_agent, output.response,  run_config=config)

#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered= result.final_output.isPHDLevelResponse
#     )

# # Main executor agent
# eigth_grade_std = Agent(
#     name = "Eight grade student",
#     instructions="""
#         1. You are an agent that answer query to a eight standard student. Keep your vocabulary simple and easy. 
#         2. If asked to give answers in most difficult level use the most hardest english terms
#     """,
#     output_type=MessageOutput,
#     output_guardrails=[PHD_guardrail]
# )

# async def og_main():
#     query = "What are trees? Explain using the most complex scientific terminology possible"
#     # query = "What are trees? Explain in simple words"
#     try:
#         result = await Runner.run(eigth_grade_std, query, run_config=config)
#         print(result.final_output)

#     except OutputGuardrailTripwireTriggered:
#         print('Agent output is not according to the expectations')


# if __name__ == "__main__":
#      asyncio.run(og_main())
#     # asyncio.run(main())










