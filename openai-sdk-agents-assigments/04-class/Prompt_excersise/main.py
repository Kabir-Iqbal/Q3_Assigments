from agents import Agent, Runner, function_tool, result
from connection import config



@function_tool
def get_wether(city:str, time:str)->str:
    return f'the wether of {city} is rainy {time} '


@function_tool
def find_resturants(country: str = "Dubai", time: str = "evening", cuisine: str = "Chinese") -> str:
    """Finds open restaurants near downtown for a given country and time."""
    return f"These {cuisine} restaurants are open {time} in {country} and near downtown: Kundan Restaurant, Zaiqa Restaurant."



@function_tool
def send_email(to: str, subject: str, body: str) -> str:
    """Sends an email to the given recipient."""
    # You can add actual sending logic later (SMTP, service API, etc.)
    return f"Email sent to {to} with subject: '{subject}' and body: '{body}'"


@function_tool
def schedule_meeting(team: str, day: str, time : str, topic: str) -> str:
    """Schedules a meeting with a given team at a specific time about a topic."""
    return f"Meeting scheduled with the {team} on {day} at {time} to discuss: {topic}."


@function_tool
def find_products(product_name: str, max_price: float, rating: str) -> str:
    """Finds products based on name, price limit, and rating preference."""
    return f"Showing top-rated {product_name} under ${max_price} with {rating} reviews."



agent = Agent(
    name = "Tools agent",
    instructions= 'You are a helpful agent',
    tools=[get_wether, find_resturants,send_email, schedule_meeting, find_products]
)

result = Runner.run_sync(
    agent,
    # 'Whats the weather going to be like in Dubai tomorrow afternoon',
    'Find some Chinese restaurants in Dubai that are open at 7 PM near downtown',
    #"Send an email to sarah@example.com saying the project deadline is moved to next Wednesday",
    # "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign",
    # "I want to buy a wireless Bluetooth headphones under $100 with good reviews",
    run_config=config
)


print(result.final_output)