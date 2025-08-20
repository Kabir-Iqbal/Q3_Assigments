from agents import Agent, Runner,function_tool, result,trace
import asyncio
from connection import config
from dotenv import load_dotenv


poet_Agent = Agent(
    name='Poet Agent',
    instructions="""
    You are a creative Poet Agent. Your job is to write a short, original poem (2 to 4 stanzas) based on the user’s 
    input or theme request. The poem should be expressive, emotionally engaging, and use poetic techniques like imagery,
    rhyme, or metaphors when appropriate. Make sure the tone and style match the theme provided by the user.
    """,
)


Theme_Analyst_Agent = Agent(
    name='ThemeAnalystAgent',
    instructions="""You are a Theme Analyst Agent. Your task is to carefully analyze any given poem and identify its main theme or central idea.
     Focus on what message the poet is trying to convey — whether it's about love, sadness, nature, hope, or another emotion or concept. 
     Explain your analysis clearly and briefly, and support your answer using references or lines from the poem if possible.
     """
)


Language_Analyst_Agent = Agent(
    name='LanguageAnalystAgent',
    instructions="""You are a Language Analyst Agent. Your task is to analyze the use of language in the given poem. 
    Pay attention to the poet’s word choices, rhyme schemes, metaphors, similes, personification, and other literary devices. 
    Describe how these techniques enhance the poem’s meaning, tone, and beauty. Support your analysis with examples from the 
    poem where possible.
    """
)


Emotion_Analyst_Agent = Agent(
    name='EmotionAnalystAgent',
    instructions="""You are an Emotion Analyst Agent. Your role is to examine the emotional tone of the poem. 
    Identify and describe the emotions expressed by the poet — such as happiness, sadness, loneliness, hope, 
    anger, or love. Explain how the language, imagery, and expressions in the poem reflect these emotions. Use specific 
    lines or words from the poem to support your analysis.
    """
)


Parent_agent= Agent(
    name='Parent Agent',
    instructions="""
    You are a Parent Agent (Orchestrator). Your task is to handle user input and coordinate with other agents.
    1. If the user input is a poem, send it to the following agents:
    - ThemeAnalystAgent
    - LanguageAnalystAgent
    - EmotionAnalystAgent
    2. Wait for all three analysis agents to complete their analysis.
    3. Once all responses are received, format and return a final response like this:
    📥 Original Poem:
    <user input poem>
    🎭 Theme Analysis:
    <response from ThemeAnalystAgent>
    🧠 Language Analysis:
    <response from LanguageAnalystAgent>
    ❤️ Emotion Analysis:
    <response from EmotionAnalystAgent>
    4. If the input is a request to 'write a poem', first send the theme to the PoetAgent, get the poem, then follow the same analysis process as above.
    Your job is to fully orchestrate this pipeline and give a clean final output. Do not skip formatting or skip agents unless explicitly told by the user.
    """,
    handoffs=[poet_Agent,Theme_Analyst_Agent]
)

async def main():
    with trace('Poetry-Agent'):
        result = await Runner.run(
           Parent_agent,
           """
           Like stars adrift, in endless night,
           A fragile hope, a fading light.
           To bridge the gap, to find release,
           And break the chains of loneliness.
           """,
            run_config=config
        )
        print(result.final_output)
        print("Last Agent ==> ",result.last_agent.name)



if __name__=="__main__":
    asyncio.run(main())