# import json        #fro read/write data in json form
# import  streamlit as st

# class BookCollection:
#     """A class to manage a collection of books, allowing users to store and organize their reading materials."""

#     def __init__(self):        # constructor Jab bhi class ka object create hoga, yeh constructor execute hoga.
#         """Initialize a new book collection with an empty list and set up file storage."""
#         self.book_list = []
#         self.storage_file = "books_data.json"
#         self.read_from_file()     #  method ko call kiya gaya hai taake agar pehle se koi data ho toh load ho jaye.

#     def read_from_file(self):
#         """Load saved books from a JSON file into memory.
#         If the file doesn't exist or is corrupted, start with an empty collection."""
#         try:
#             with open(self.storage_file, "r") as file:        # with function se storage_file variable ko khola gya he as read
#                 self.book_list = json.load(file)              # Agar file exist karti hai toh uska content self.book_list mein load ho jata hai.
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.book_list = []

#     def save_to_file(self):
#         """Store the current book collection to a JSON file for permanent storage."""
#         with open(self.storage_file, "w") as file:            # with function se storage_file variable ko khola gya he as write      
#             json.dump(self.book_list, file, indent=4)         #json.dump() ka use kiya gaya hai jo list ko JSON format mein convert karke file mein likhta hai.

#     def create_new_book(self):
#         """Add a new book to the collection by gathering information from the user."""
#         book_title = input("Enter book title: ")
#         book_author = input("Enter author: ")
#         publication_year = input("Enter publication year: ")
#         book_genre = input("Enter genre: ")
#         is_book_read = (
#             input("Have you read this book? (yes/no): ").strip().lower() == "yes"
#         )

#         new_book = {
#             "title": book_title,
#             "author": book_author,
#             "year": publication_year,
#             "genre": book_genre,
#             "read": is_book_read,
#         }

#         self.book_list.append(new_book)            # booklist m new dictionary add krdi
#         self.save_to_file()                       # save_to_file() function ko call kiya taky json m data save hojae
#         print("Book added successfully!\n")

#     def delete_book(self):
#         """Remove a book from the collection using its title."""
#         book_title = input("Enter the title of the book to remove: ")

#         for book in self.book_list:            # check kr raha hu book_list m search kiya huwa book he
#             if book["title"].lower() == book_title.lower():  
#                 self.book_list.remove(book)     # agr book milljata he to remove kr raha hu
#                 self.save_to_file()             # then update krky save kr raah  hu 
#                 print("Book removed successfully!\n")
#                 return
#         print("Book not found!\n")

#     def find_book(self):
#         """Search for books in the collection by title or author name."""
#         search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
#         search_text = input("Enter search term: ").lower()
#         found_books = [               # user ka serach kiya huwa book check kr raha hu 
#             book
#             for book in self.book_list       
#             if search_text in book["title"].lower()
#             or search_text in book["author"].lower()
#         ]

#         if found_books:         
#             print("Matching Books:")     # agr book mill jati he toh display p show kr raha hu
#             for index, book in enumerate(found_books, 1):
#                 reading_status = "Read" if book["read"] else "Unread"
#                 print(
#                     f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
#                 )
#         else:
#             print("No matching books found.\n")

#     def update_book(self):
#         """Modify the details of an existing book in the collection."""
#         book_title = input("Enter the title of the book you want to edit: ")
#         for book in self.book_list:
#             if book["title"].lower() == book_title.lower():
#                 print("Leave blank to keep existing value.")
#                 book["title"] = input(f"New title ({book['title']}): ") or book["title"]
#                 book["author"] = (
#                     input(f"New author ({book['author']}): ") or book["author"]
#                 )
#                 book["year"] = input(f"New year ({book['year']}): ") or book["year"]
#                 book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
#                 book["read"] = (
#                     input("Have you read this book? (yes/no): ").strip().lower()
#                     == "yes"
#                 )
#                 self.save_to_file()
#                 print("Book updated successfully!\n")
#                 return
#         print("Book not found!\n")

#     def show_all_books(self):
#         """Display all books in the collection with their details."""
#         if not self.book_list:
#             print("Your collection is empty.\n")
#             return

#         print("Your Book Collection:")
#         for index, book in enumerate(self.book_list, 1):
#             reading_status = "Read" if book["read"] else "Unread"
#             print(
#                 f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
#             )
#         print()

#     def show_reading_progress(self):
#         """Calculate and display statistics about your reading progress."""
#         total_books = len(self.book_list)
#         completed_books = sum(1 for book in self.book_list if book["read"])
#         completion_rate = (
#             (completed_books / total_books * 100) if total_books > 0 else 0
#         )
#         print(f"Total books in collection: {total_books}")
#         print(f"Reading progress: {completion_rate:.2f}%\n")

#     # def start_application(self):
#     #     """Run the main application loop with a user-friendly menu interface."""
#     #     while True:
#     #         print("📚 Welcome to Your Book Collection Manager! 📚")
#     #         print("1. Add a new book")
#     #         print("2. Remove a book")
#     #         print("3. Search for books")
#     #         print("4. Update book details")
#     #         print("5. View all books")
#     #         print("6. View reading progress")
#     #         print("7. Exit")
#     #         user_choice = input("Please choose an option (1-7): ")

#     #         if user_choice == "1":
#     #             self.create_new_book()
#     #         elif user_choice == "2":
#     #             self.delete_book()
#     #         elif user_choice == "3":
#     #             self.find_book()
#     #         elif user_choice == "4":
#     #             self.update_book()
#     #         elif user_choice == "5":
#     #             self.show_all_books()
#     #         elif user_choice == "6":
#     #             self.show_reading_progress()
#     #         elif user_choice == "7":
#     #             self.save_to_file()
#     #             print("Thank you for using Book Collection Manager. Goodbye!")
#     #             break
#     #         else:
#     #             print("Invalid choice. Please try again.\n")



# if __name__ == "__main__":
#     book_manager = BookCollection()
#     book_manager.start_application()


import json
import streamlit as st
import os


IMAGE_FOLDER = "book_images"

st.markdown(
    f"""
    <style>
        img {{
            width: 200px !important;
            height: 300px !important;
            object-fit: contain;
        }}

        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: #1f2937;
            padding-top: 20px;
        }}
    
        [data-testid="stSidebar"] h1 {{
            color: white;
            text-align: center;
            font-size: 20px;
        }}

        /* Buttons Styling */
        div.stButton > button {{
            background-color: #4F46E5;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease-in-out;
        }}

        div.stButton > button:hover {{
            background-color: #4338CA;
            transform: scale(1.05);
        }}

        /* Input Fields */
        div.stTextInput > div > input, 
        div.stFileUploader > div > div > button {{
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
        }}

        /* Success Message */
        div[data-testid="stSuccess"] {{
            background-color: #34D399;
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 8px;
        }}

        /* Book Cards */
        .book-card {{
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: center;
        }}

        .book-card img {{
            width: 120px;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 10px;
        }}

        .book-card h4 {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .book-card p {{
            font-size: 14px;
            color: #6B7280;
        }}

        /* Footer */
        .footer {{
            text-align: center;
            font-size: 14px;
            color: white;
            margin-top: 20px;
        }}

        /* Sidebar Radio Button Title */
        section[data-testid="stSidebar"] label {{
            color: white !important;
        }}

        /* Sidebar Radio Button Options */
        section[data-testid="stSidebar"] div[role="radiogroup"] div {{
            color: white !important;
        }}

    """,
    unsafe_allow_html=True
)



 #book detail card function bnaay or usmy book ka parameter dala 
def display_book_card(book):
    # Book details ka ek card bnaya jsmy sarri details dali 

    with st.container():
        # 📌 Pehly book ki image show krwayi
        if "image" in book and book["image"]:
            image_path = os.path.join(book["image"])
            st.image(image_path, caption="Book",  width=150)

        # 📌 bad m book ka title 
        st.subheader(f"📖 {book['title']}")

        # 📌 Baki details
        st.write(f"✍️ **Author:** {book['author']}")
        st.write(f"📅 **Year:** {book['year']}")
        st.write(f"📚 **Genre:** {book['genre']}")

        st.markdown("---")  # 🔹 Separator line
    

   # el class instructor bnaya taky bohut see copy le sku
class BookCollection:
    #ek instructor bnaya taky hr function m run krsku
    def __init__(self):
        # ek booklist ka variable bnaya jsmy empty array dala 
        self.book_list = []
        # yahan ek storage_file ka variable bnaya jsmy json data file ka path diya 
        self.storage_file = "books_data.json"
        # asy read_from file function run kiya
        self.read_from_file()
    
    # read from file function bnaya or instructor ka key parameter dala 
    def read_from_file(self):

        try:
            # json file ko as read open kiya 
            with open(self.storage_file, "r") as file:
                # yahan book list variable m json ki file load krwayi
                self.book_list = json.load(file)
        #yahan error handle kiya 
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
    # save_to_file function bnaya or usmy self parameter dala 
    def save_to_file(self):
        #json file ko open kiya as write 
        with open(self.storage_file, "w") as file:
            # json.dumb method se json m data save kiya 
            json.dump(self.book_list, file, indent=4)

    # add boook ka function bnaya jsmy self constructor dala  or baki books ke data parameters       
    def add_book(self, title, author, year, genre, read, image_filename):
        # Yahan ek dictionary create ki taky sara data ek dict m add kru 
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read,
            "image": image_filename
        }
        # yahan book_list variable m new book variable add kiya 
        self.book_list.append(new_book)
        # last m save function challaky data save ki
        self.save_to_file()

    # remove function create kiya 
    def remove_book(self, title):
        # yahan check kiya k book_list m user ka titele he age he to wo delete krky baki save krdo
        self.book_list = [
            book 
            for book in self.book_list
            if book["title"].lower() != title.lower()]
        
        self.save_to_file()
    # yaahn books find function bnaya or user se search text liya 
    def find_book(self, search_text):
        # yahan check kiya k user ka search kiya huwa title ya author m he to dikha do 
        return [book
                for book in self.book_list 
                if search_text.lower() in book["title"].lower() 
                or search_text.lower() in book["author"].lower()]
    
    #update function bnaya or asmy books ki tamam parameters dale or old title ka b parameter liya 
    def update_book(self, old_title, new_title, new_author, new_year, new_genre, new_read,image_filename):
        for book in self.book_list:
            # yahan check kiya gar user ka new title old title se match ho  raha he 
            if book["title"].lower() == old_title.lower():
                # agr ho raha he to update krdo
                book.update({
                "title": new_title,
                "author": new_author,
                "year": new_year,
                "genre": new_genre,
                "read": new_read,
                "image": image_filename if book_image else book["image"]  # ✅ Save only the file name
            })
                self.save_to_file() # fr save kr liya 
                break

  

   


    # get books ka function bnaya jsmy sarry books leye 
    def get_books(self):
        return self.book_list

    # reading books function bnaya 
    def reading_progress(self):
        #yahan total books ki len check ki
        total_books = len(self.book_list)
        # yahan sum kiya ky book_list m kitny books read waly hen
        completed_books = sum(1 for book in self.book_list if book["read"])
         # yahan total books ko return kiya      or reading progres return ki
        return total_books, (completed_books / total_books * 100 if total_books else 0)
    
   


    

# Streamlit UI
st.title("📚 Book Collection Manager")
# bookmanager variable m sarra bookcollection function store keye 
book_manager = BookCollection()
# options bnaye 
options = ["Add a new book",
           "Remove a book",
           "Search for books",
           "Update book details", 
           "View all books", 
           "View reading progress"]

# Sidebar title
st.sidebar.title("📖 Menu")


# Sidebar slider for selection
choice = st.sidebar.radio("Select an action:", options)

# ---- Sidebar Footer (Fixed at Bottom) ----
st.sidebar.markdown(
    """
    <style>
        .sidebar-footer {
            color: white;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }
        .sidebar-footer hr {
            border: 1px solid white;
        }
    </style>
    <br><br><br><br><br><br><br> <!-- Space to push footer down -->
    <hr class="sidebar-footer"> <!-- Separator line -->
    <p class="sidebar-footer">📝 <b>Developed by Kabir Iqbal</b></p>
    <p class="sidebar-footer">📅 2025 | Version 1.0</p>
    """,
    unsafe_allow_html=True
)


# فولڈر بنائیں اگر موجود نہ ہو
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# agr user ki choice new book p select kre toh ye sara inputs show ho
if choice == "Add a new book":
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    # yahan file_uploader input diya taky user jpg png or jpeg m dal sky
    book_image = st.file_uploader("Upload Book Cover", type=["jpg", "png", "jpeg"])
    read = st.checkbox("Have you read this book?")
   

    if st.button("Add Book"):
        # yahan check kiya k book ki image availbe he toh 
        if book_image:
            #image_filename variable bnaya or usmy iamge folder ka patha diya or image ka name 
            image_filename = os.path.join(IMAGE_FOLDER, book_image.name)
            # image_filename open ki as wb  
            with open(image_filename, "wb") as f:
                # fr getbuffer() function se image save krdi
                f.write(book_image.getbuffer())
        # yahan sarry book ki data save krdi 
        book_manager.add_book(title, author, year, genre, read, image_filename)
        st.success("Book added successfully!")

elif choice == "Remove a book":
    st.subheader("Remove a Book")
    title = st.text_input("Enter the book title to remove")
    if st.button("Remove Book"):
        book_manager.remove_book(title)
        st.success("Book removed successfully!")

elif choice == "Search for books":
    st.subheader("Search your Book")
    search_text = st.text_input("Enter title or author name")
    if st.button("Search"):
        results = book_manager.find_book(search_text)
        for book in results:
            # st.write(book)
            display_book_card(book)  # 👈 کارڈ میں دکھانے کے لیے فنکشن کال کریں
        if not results:
            st.warning("No books found")

elif choice == "Update book details":
    st.subheader("Update your Book")
    old_title = st.text_input("Enter the title of the book to update")
    new_title = st.text_input("New Title", old_title)
    new_author = st.text_input("New Author")
    new_year = st.text_input("New Publication Year")
    new_genre = st.text_input("New Genre")
    new_read = st.checkbox("Have you read this book?")
    book_image = st.file_uploader("Upload Book Cover", type=["jpg", "png", "jpeg"])
    if st.button("Update Book"):
         # yahan check kiya k book ki image availbe he toh 
        if book_image:
            #image_filename variable bnaya or usmy iamge folder ka patha diya or image ka name 
            image_filename = os.path.join(IMAGE_FOLDER, book_image.name)
            # image_filename open ki as wb  
            with open(image_filename, "wb") as f:
                # fr getbuffer() function se image save krdi
                f.write(book_image.getbuffer())
        book_manager.update_book(old_title, new_title, new_author, new_year, new_genre, new_read,image_filename)
        st.success("Book updated successfully!")

elif choice == "View all books":
    st.subheader("Your Books")
    books = book_manager.get_books()
    for book in books:
        #st.write(book)
        display_book_card(book)

elif choice == "View reading progress":
    st.subheader("Your Reading ratio:")
    total, progress = book_manager.reading_progress()
    st.write(f"Total books: {total}")
    st.write(f"Reading progress: {progress:.2f}%")
