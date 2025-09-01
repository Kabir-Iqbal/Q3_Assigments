# bank_account = BankAccount(
#     account_number="ACC-789456",
#     customer_name="Fatima Khan",
#     account_balance=75500.50,
#     account_type="savings"
# )

# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from connection import config
# from pydantic import BaseModel

# class CustomerInfo(BaseModel):
#     account_number: str
#     customer_name: str
#     account_balance: int
#     account_type: str

# customer_Information = CustomerInfo(
#     account_number="ACC-789456",
#     customer_name="Fatima Khan",
#     account_balance=75500,
#     account_type="savings"
# )

# @function_tool
# def customerData(wrapper: RunContextWrapper[CustomerInfo]):
#     return f'''Customer Name: {wrapper.context.customer_name}, Account Number: {wrapper.context.account_number} 
#     Customer Balance : {wrapper.context.account_balance}, Account type : {wrapper.context.account_type} 
#     '''

# Bank_agent = Agent(
#     name='Bank Agent',
#     instructions="""
#     You are a bank agent. 
#     If the user asks anything about customer details (name, account number, balance, or type),
#     you MUST call the tool `customerData`. Never try to answer directly.
#     """,
#     tools=[customerData]
# )

# async def main():
#     try:
#         result = await Runner.run(
#             Bank_agent,
#             'Whats Customer name and customers bank account and account balance and which is account type?',
#             run_config=config,
#             context=customer_Information
#         )
#         print(result.final_output)
#     except Exception as e:
#         print(f'Invalid query: {e}')

# if __name__ == "__main__":
#     asyncio.run(main())



# # 2. STUDENT PROFILE CONTEXT

# student = StudentProfile(
#     student_id="STU-456",
#     student_name="Hassan Ahmed",
#     current_semester=4,
#     total_courses=5
# )

# import asyncio
# from agents import Agent, Runner, function_tool, RunContextWrapper
# from connection import config
# from pydantic import BaseModel

# class StudentInfo(BaseModel):
#     student_id: str
#     student_name:str
#     current_semester:int
#     total_courses:int

# Student_Information = StudentInfo(
#     student_id="STU-456",
#     student_name="Hassan Ahmed",
#     current_semester=4,
#     total_courses=5
# )

# @function_tool
# def StudentData(wrapper: RunContextWrapper[StudentInfo]):
#     return f'''Student Name: {wrapper.context.student_name}, Student Id: {wrapper.context.student_id} 
#     Total courses : {wrapper.context.total_courses}, Current Semester: {wrapper.context.current_semester} 
#     '''

# Academy_agent = Agent(
#     name='Academy agent',
#     instructions="""
#     You are a academy agent. 
#     If the user asks anything about student details (name, Id Couses, Semester),
#     you MUST call the tool `StudentData`. Never try to answer directly.
#     """,
#     tools=[StudentData]
# )

# async def main():
#     try:
#         result = await Runner.run(
#             Academy_agent,
#             'Whats Student name , StudentId , and in which semester and how many courses are doing?',
#             run_config=config,
#             context=Student_Information
#         )
#         print(result.final_output)
#     except Exception as e:
#         print(f'Invalid query: {e}')

# if __name__ == "__main__":
#     asyncio.run(main())





# # 3. LIBRARY BOOK CONTEXT
# library_book = LibraryBook(
#     book_id="BOOK-123",
#     book_title="Python Programming",
#     author_name="John Smith",
#     is_available=True
# )



import asyncio
from agents import Agent, Runner, function_tool, RunContextWrapper
from connection import config
from pydantic import BaseModel

class LibraryInfo(BaseModel):
    book_id:str
    book_title:str
    author_name:str
    is_available:bool

Library_Information = LibraryInfo(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)

@function_tool
def LibraryData(wrapper: RunContextWrapper[LibraryInfo]):
    return f'''Book Id: {wrapper.context.book_id}, Book title: {wrapper.context.book_title} 
    Author Name : {wrapper.context.author_name}, Is available: {wrapper.context.is_available} 
    '''

Library_agent = Agent(
    name='Library agent',
    instructions="""
    You are a Library agent. 
    If the user asks anything about Books details (author name,Book Id,Book Title, is available),
    you MUST call the tool `LibraryData`. Never try to answer directly.
    """,
    tools=[LibraryData]
)

async def main():
    try:
        result = await Runner.run(
            Library_agent,
            'Whats Book Id , Book Title,  Author name , and  is it available?',
            run_config=config,
            context=Library_Information
        )
        print(result.final_output)
    except Exception as e:
        print(f'Invalid query: {e}')

if __name__ == "__main__":
    asyncio.run(main())