import click
import json
import os   # to check the file exits
import streamlit as st

TODO_File = "todo.json"

# def load_tasks():
#     if not os.path.exists(TODO_File):  # اگر فائل موجود ہو
#         return []
#     with open(TODO_File, "r") as file:  # فائل کو ریڈ موڈ میں کھولو
#         return json.load(file)  # JSON فائل سے ڈیٹا لوڈ کرو

    
# def save_task(tasks):
#     with open(TODO_File, "w") as file:  # فائل کو لکھنے کے موڈ میں کھولو
#         json.dump(tasks, file, indent=4)  # JSON میں فارمیٹڈ طریقے سے سیو کرو


# @click.group()
# def cli():
#     """ Simple Todo List Manager """
#     pass

# @click.command()
# @click.argument("task" , type= str)

# def add(task):
#     """ Add a new task to the list """
#     tasks = load_tasks()
#     tasks.append({"task" :task, "done": False })
#     save_task(tasks)
#     click.echo(f"Thanks added successfully : {task}")

# cli.add_command(add)


# @click.command()
# def list():
#     tasks = load_tasks()
#     if not tasks:
#         click.echo("no tasks found")
#         return
#     for index, task in enumerate(tasks, 1):
#         status = "pass" if task['done'] else 'x'
#         click.echo(f"{index}. {task ['task']} [{status}]")


# @click.command()
# @click.argument("task_number", type= int)
# def complete(task_number):
#     """ Mark a Task as completed """
#     tasks = load_tasks()
#     if 0 < task_number <= len(tasks):
#         tasks[task_number -1]["done"] = True
#         save_task(tasks)
#         click.echo(f"Task {task_number} marked as completed ")
#     else:
#         click.echo(f"Invaild task number {task_number}")

# @click.command()
# @click.argument("task_number", type= int)
# def remove(task_number):
#     """Remove a task from the list """
#     tasks = load_tasks()
#     if 0 < task_number <= len(tasks):
#         removed_task = tasks.pop(task_number -1)  # ✅ متغیر کا نام بہتر کرو
#         save_task(tasks)
#         click.echo(f"Removed task: {removed_task['task']}")  # ✅ صرف ٹاسک کا نام دکھاؤ
#     else:
#         click.echo("Invaild task ")

    
# cli.add_command(add)
# cli.add_command(list)
# cli.add_command(complete)
# cli.add_command(remove)





def load_tasks():
    """ ٹاسکس کو لوڈ کرے، اگر فائل موجود نہ ہو تو خالی لسٹ ریٹرن کرے۔ """
    if not os.path.exists(TODO_File):
        return []
    with open(TODO_File, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """ ٹاسکس کو JSON فائل میں سیو کرے۔ """
    with open(TODO_File, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """ نیا ٹاسک ایڈ کرے۔ """
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def complete_task(task_index):
    """ ٹاسک مکمل کرے۔ """
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)

def remove_task(task_index):
    """ ٹاسک کو ڈیلیٹ کرے۔ """
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)

# --- Custom CSS ---
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #4CAF50;
    font-size: 3rem;
}
            
/* Add Task button ka width full nahi hoga */
div.stButton > button:not(:nth-of-type(1)) {
    width: 100%;
}

/* General Button Styling */
div.stButton > button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 2px 6px;
    margin: 1px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
            
div.stButton > button:hover {
    background-color: #45a049;
}

div.stTextInput > label {
    font-weight: bold;
    font-size: 1.2rem;
    color: #333;
}

div.stTextInput > div > input {
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #4CAF50;
}
/* Tasks List کو Vertically Center کرنے کے لیے */
div.stMarkdown {
    margin-top: auto !important;
    margin-bottom: auto !important;
}            

.stCheckbox > label {
    font-weight: bold;
    font-size: 1rem;
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)





# --- Streamlit UI ---
st.title("📌 To-Do List App")



# --- ٹاسک ایڈ کرنا ---
new_task = st.text_input("Enter your task:")
if st.button("Add Task"):
    if new_task:
        add_task(new_task)
        # st.toast(f"Task '{new_task}' added successfully!", icon="✅")
        # st.rerun()
            # سیشن میں ویلیو اسٹور کریں
        st.session_state.task_added = True
        st.session_state.task_name = new_task
        st.rerun()  # UI کو ریفریش کریں 


# سیشن میں چیک کریں کہ پیغام دکھانا ہے یا نہیں
if "task_added" in st.session_state and st.session_state.task_added:
    st.success(f"Task '{st.session_state.task_name}' added successfully!", icon="✅")
    st.session_state.task_added = False  # اگلی بار چھپانے کے لیے False کریں

# --- ٹاسکس دکھانا اور کنٹرولز ---
tasks = load_tasks()
if tasks:
    st.subheader("Your Tasks:")
    for index, task in enumerate(tasks):
        col1, col2, col3 = st.columns([6, 2, 2])
        
        with col1:
            st.write(f"{index + 1}. {task['task']} {'✅' if task['done'] else '❌'}")
        
        with col2:
            if not task["done"]:
                if st.button(f"✔ Complete {index+1}", key=f"complete_{index}"):
                    complete_task(index)
                    st.rerun()

        
        with col3:
            if st.button(f"🗑 Remove {index+1}", key=f"remove_{index}"):
                remove_task(index)
                st.rerun()

else:
    st.write("No tasks found. Add a new one!")
