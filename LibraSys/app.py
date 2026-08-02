import streamlit as st
from oop import Library
import pandas as pd
import plotly.express as px
import time

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Main background */
.stApp{
    background-color:#0E1117;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background:linear-gradient(135deg,#1f2937,#111827);
    padding:20px;
    border-radius:15px;
    border:1px solid #374151;
    box-shadow:0px 6px 15px rgba(0,0,0,.4);
}

/* Metric Label */
[data-testid="stMetricLabel"]{
    color:white;
    font-size:18px;
    font-weight:bold;
}

/* Metric Value */
[data-testid="stMetricValue"]{
    color:#00E676;
    font-size:36px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#1f1f2e;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "Manage your books efficiently with a simple and interactive interface."
)
# -----------------------------
# Load Library
# -----------------------------
library = Library()
library.load_books()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2232/2232688.png",
    width=90
)

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2232/2232688.png",
    width=90
)

st.sidebar.title("Library Management")
st.sidebar.success("Version 1.0")

st.sidebar.divider()

menu = st.sidebar.radio(
    "Choose an option",
    [
        "🏠 Dashboard",
        "📚 View Books",
        "➕ Add Book",
        "🔍 Search Book",
        "📤 Issue Book",
        "📥 Return Book",
        "🗑 Remove Book"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------
if menu == "🏠 Dashboard":

    title = st.empty()

    text = "📚 LibraSys"

    for i in range(len(text) + 1):
        title.markdown(f"# {text[:i]}")
        time.sleep(0.08)

    st.markdown("""
    ### Smart Library Management Dashboard

    Manage books, issue, return and track your library books in one place.
    """)

    
    st.info(
    "👋 Welcome! Manage books, issue and return them, and monitor your library from one dashboard."
    )

    total = len(library.books)
    available = len([b for b in library.books if b.available])
    issued = total - available

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="📚 Total Books",
        value=total
    )

    col2.metric(
        label="✅ Available",
        value=available
    )

    col3.metric(
        label="📕 Issued",
        value=issued
    )

    st.divider()

    chart_data = pd.DataFrame({
        "Status": ["Available", "Issued"],
        "Books": [available, issued]
    })

    fig = px.pie(
        chart_data,
        names="Status",
        values="Books",
        title="Library Book Distribution",
        hole=0.45
    )

    st.subheader("📊 Library Overview")
    
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Quick Statistics
    # -----------------------------

    st.subheader("📊 Quick Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📚 Total Books : {total}")

    with col2:
        percentage = 0 if total == 0 else round((available / total) * 100, 2)
        st.success(f"📈 Availability : {percentage}%")

    st.divider()

    # -----------------------------
    # Recent Books
    # -----------------------------

    st.subheader("📖 Recent Books")

    if total == 0:
        st.info("No books available.")

    else:

        data = []

        for book in library.books:

            data.append({
                "Book ID": book.book_id,
                "Book Name": book.name,
                "Author": book.author,
                "Status": "🟢 Available" if book.available else "🔴 Issued",
                "Issued To": book.issued_to if book.issued_to else "-"
            })

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Library Report",
            data=csv,
            file_name="library_books.csv",
            mime="text/csv"
        )
# -----------------------------
# Add Book
# -----------------------------
elif menu == "➕ Add Book":

    st.title("➕ Add New Book")

    with st.form("add_book_form"):

        book_id = st.number_input(
            "Book ID",
            min_value=1,
            step=1
        )

        name = st.text_input("Book Name")

        author = st.text_input("Author")

        submitted = st.form_submit_button("Add Book")

        if submitted:

            if name.strip() == "":
                st.error("Book name cannot be empty.")

            elif author.strip() == "":
                st.error("Author name cannot be empty.")

            else:

                duplicate = False

                for book in library.books:
                    if book.book_id == book_id:
                        duplicate = True
                        break

                if duplicate:
                    st.error("Book ID already exists.")

                else:
                    from oop import Book

                    new_book = Book(book_id, name, author)

                    library.add_book(new_book)

                    st.success("Book added successfully!")
                    st.balloons()
# --------------------------------------------------------
# View Books
# --------------------------------------------------------

elif menu == "📚 View Books":

    st.title("📚 Library Books")

    if len(library.books) == 0:
        st.warning("No books available.")
    else:

        data = []

        for book in library.books:

            data.append({
                "Book ID": book.book_id,
                "Book Name": book.name,
                "Author": book.author,
                "Status": "🟢 Available" if book.available else "🔴 Issued",
                "Issued To": book.issued_to if book.issued_to else "-"
            })

        df = pd.DataFrame(data)

        search = st.text_input("🔍 Search Book")

        if search:

            df = df[
                df["Book Name"].str.contains(search, case=False)
                |
                df["Author"].str.contains(search, case=False)
                |
                df["Book ID"].astype(str).str.contains(search)
            ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
# --------------------------------------------------------
# Search Book
# --------------------------------------------------------

elif menu == "🔍 Search Book":

    st.title("🔍 Search Book")

    if len(library.books) == 0:
        st.warning("No books available in the library.")

    else:

        search_type = st.radio(
            "Search By",
            ["Book ID", "Book Name"]
        )

        if search_type == "Book ID":

            book_id = st.number_input(
                "Enter Book ID",
                min_value=1,
                step=1
            )

            if st.button("Search"):

                found = False

                for book in library.books:

                    if book.book_id == book_id:

                        found = True

                        st.success("Book Found")

                        st.write(f"**Book ID:** {book.book_id}")
                        st.write(f"**Book Name:** {book.name}")
                        st.write(f"**Author:** {book.author}")
                        st.write(
                            f"**Status:** {'Available' if book.available else 'Issued'}"
                        )

                        if book.issued_to:
                            st.write(f"**Issued To:** {book.issued_to}")

                        break

                if not found:
                    st.error("Book not found.")

        else:

            name = st.text_input("Enter Book Name")

            if st.button("Search"):

                found_books = []

                for book in library.books:

                    if name.lower() in book.name.lower():

                        found_books.append(book)

                if len(found_books) == 0:

                    st.error("Book not found.")

                else:

                    st.success(f"{len(found_books)} book(s) found.")

                    data = []

                    for book in found_books:

                        data.append({
                            "Book ID": book.book_id,
                            "Book Name": book.name,
                            "Author": book.author,
                            "Status": "Available" if book.available else "Issued",
                            "Issued To": book.issued_to if book.issued_to else "-"
                        })

                    st.dataframe(
                        pd.DataFrame(data),
                        use_container_width=True,
                        hide_index=True
                    )
# --------------------------------------------------------
# Issue Book
# --------------------------------------------------------

elif menu == "📤 Issue Book":

    st.title("📤 Issue Book")

    available_books = [book for book in library.books if book.available]

    if len(available_books) == 0:
        st.warning("No books are currently available for issue.")

    else:

        selected_book = st.selectbox(
            "Select Book",
            available_books,
            format_func=lambda b: f"{b.book_id} - {b.name}"
        )

        st.markdown("### 📖 Book Details")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Book ID:** {selected_book.book_id}")
            st.write(f"**Book Name:** {selected_book.name}")

        with col2:
            st.write(f"**Author:** {selected_book.author}")
            st.write("**Status:** 🟢 Available")

        borrower = st.text_input("Borrower Name")

        if st.button("Issue Book"):

            if borrower.strip() == "":
                st.error("Borrower name cannot be empty.")

            else:

                success, message = library.issue_book_gui(
                    selected_book.book_id,
                    borrower
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)
# --------------------------------------------------------
# Return Book
# --------------------------------------------------------

elif menu == "📥 Return Book":

    st.title("📥 Return Book")

    issued_books = [book for book in library.books if not book.available]

    if len(issued_books) == 0:
        st.warning("No books are currently issued.")

    else:

        selected_book = st.selectbox(
            "Select Issued Book",
            issued_books
        )

        st.write(f"**Issued To:** {selected_book.issued_to}")

        if st.button("Return Book"):

            success, message = library.return_book_gui(
                selected_book.book_id
            )

            if success:
                st.success(message)
                st.rerun()

            else:
                st.error(message)
# --------------------------------------------------------
# Remove Book
# --------------------------------------------------------

elif menu == "🗑 Remove Book":

    st.title("🗑 Remove Book")

    if len(library.books) == 0:

        st.warning("No books available.")

    else:

        selected_book = st.selectbox(
            "Select Book",
            library.books
        )

        st.write(f"**Book ID:** {selected_book.book_id}")
        st.write(f"**Author:** {selected_book.author}")
        st.write(f"**Status:** {'Available' if selected_book.available else 'Issued'}")

        confirm = st.checkbox(
            "I understand this action cannot be undone."
        )

        if st.button("🗑 Delete Book"):

            if not confirm:
                st.error("Please confirm before deleting.")

            else:

                success, message = library.remove_book_gui(
                    selected_book.book_id
                )

                if success:
                    st.success(message)
                    st.rerun()

                else:
                    st.error(message)
# --------------------------------------------------------
# Footer
# --------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
        📚 Library Management System <br>
        Developed by <b>Saurabh Ravindra Bhonsle</b> ❤️ using Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)