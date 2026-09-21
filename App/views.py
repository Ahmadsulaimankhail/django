from django.shortcuts import render, redirect
from .forms import Entry,LendingForm,Addmember,ReturnForm
import json


# =========================
# CREATE BOOK
# =========================
def home(request):

    if request.method == "POST":

        form = Entry(request.POST, request.FILES)

        if form.is_valid():

            dic = {
                "Book_ID": form.cleaned_data["bookId"],
                "Book_Name": form.cleaned_data["bookName"],
                "Author": form.cleaned_data["author"],
                "Release_Date": str(form.cleaned_data["releaseDate"]),
                "Publisher": form.cleaned_data["publisher"],
                "City": form.cleaned_data["city"],
                "Quantity": form.cleaned_data["quantity"],
                "Description": form.cleaned_data["description"],
                "Image": str(form.cleaned_data["image"]),
                "Category": form.cleaned_data["category"],
                "Email": form.cleaned_data["email"],
                "Phone_Number": form.cleaned_data["phoneNumber"],
            }

            try:
                with open("new.json", "r") as file:
                    allData = json.load(file)

                if isinstance(allData, dict):
                    allData = [allData]

            except (FileNotFoundError, json.JSONDecodeError):
                allData = []

            # Add new book
            allData.append(dic)

            # Save everything back into JSON
            with open("new.json", "w") as file:
                json.dump(allData, file, indent=4)

            return redirect("Prograss")

    else:
        form = Entry()

    return render(
        request,
        "home.html",
        {
            "form": form
        }
    )


# =========================
# SHOW ALL BOOKS
# =========================
def prograss(request):

    try:
        with open("all_books.json", "r") as file:
            allData = json.load(file)

        if isinstance(allData, dict):
            allData = [allData]

    except (FileNotFoundError, json.JSONDecodeError):
        allData = []

    return render(
        request,
        "showbook.html",
        {
            "allData": allData
        }
    )

# =========================
# EDIT BOOK
# =========================
# def edit_book(request, book_id):

#     # Load books
#     try:
#         with open("new.json", "r") as file:
#             allData = json.load(file)

#         if isinstance(allData, dict):
#             allData = [allData]

#     except (FileNotFoundError, json.JSONDecodeError):
#         allData = []

#     # Find the book
#     selected_book = None

#     for book in allData:

#         if str(book["Book_ID"]) == str(book_id):
#             selected_book = book
#             break

#     # If book does not exist
#     if selected_book is None:
#         return redirect("Prograss")

#     # =========================
#     # UPDATE BOOK
#     # =========================
#     if request.method == "POST":

#         form = Entry(request.POST, request.FILES)

#         if form.is_valid():

#             selected_book["Book_ID"] = form.cleaned_data["bookId"]

#             selected_book["Book_Name"] = form.cleaned_data["bookName"]

#             selected_book["Author"] = form.cleaned_data["author"]

#             selected_book["Release_Date"] = str(
#                 form.cleaned_data["releaseDate"]
#             )

#             selected_book["Publisher"] = form.cleaned_data["publisher"]

#             selected_book["City"] = form.cleaned_data["city"]

#             selected_book["Quantity"] = form.cleaned_data["quantity"]

#             selected_book["Description"] = form.cleaned_data["description"]

#             selected_book["Category"] = form.cleaned_data["category"]

#             selected_book["Email"] = form.cleaned_data["email"]

#             selected_book["Phone_Number"] = form.cleaned_data["phoneNumber"]

#             # Image
#             image = form.cleaned_data.get("image")

#             # Only replace image when user selected a new image
#             if image:
#                 selected_book["Image"] = str(image)

#             # Save updated data
#             with open("new.json", "w") as file:
#                 json.dump(allData, file, indent=4)

#             return redirect("Prograss")

#     # =========================
#     # SHOW EXISTING DATA
#     # =========================
#     else:

#         form = Entry(
#             initial={
#                 "bookId": selected_book["Book_ID"],

#                 "bookName": selected_book["Book_Name"],

#                 "author": selected_book["Author"],

#                 "releaseDate": selected_book["Release_Date"],

#                 "publisher": selected_book["Publisher"],

#                 "city": selected_book["City"],

#                 "quantity": selected_book["Quantity"],

#                 "description": selected_book["Description"],

#                 "category": selected_book["Category"],

#                 "email": selected_book["Email"],

#                 "phoneNumber": selected_book["Phone_Number"],
#             }
#         )

#     return render(
#         request,
#         "edit_book.html",
#         {
#             "form": form,
#             "book": selected_book
#         }
#     )

def edit_book(request, book_id):
    with open("new.json", "r") as file:
        users = json.load(file)
    user = next(
        (user for user in users if user['Book_ID'] == book_id),
        None
    )
    if request.method =="POST":
        user["Book_ID"] = int(request.POST.get("bookId"))
        user["Book_Name"] = request.POST.get("bookName")
        user["Author"] = request.POST.get("author")
        user["Release_Date"] = request.POST.get("releaseDate")
        user["Publisher"] = request.POST.get("publisher")
        user["City"] = request.POST.get("city")
        user["Quantity"] = int(request.POST.get("quantity"))
        user["Category"] = request.POST.get("category")
        user["Email"] = request.POST.get("email")
        user["Phone_Number"] = request.POST.get("phoneNumber")
        user["Description"] = request.POST.get("description")

        # If a new image was selected
        if request.FILES.get("image"):
            image = request.FILES["image"]
            user["Image"] = image.name

        with open("new.json", "w") as file:
            json.dump(users, file, indent=4)
        return redirect("Prograss")
    return render(request,'editform.html',{"user": user})



# =========================
# DELETE BOOK
# =========================
def delete_book(request, book_id):

    if request.method == "POST":
        with open("new.json", "r") as file:
            allData = json.load(file)
        for i in allData:
            if book_id == i['Book_ID']:
                allData.remove(i)
                break   

        # Save updated JSON
        with open("new.json", "w") as file:
            json.dump(allData, file, indent=4)

    return redirect("Prograss")


# =========================
# LENDING BOOK PAGE
# =========================
def lendingBook(request):

    if request.method == "POST":

        form = LendingForm(request.POST)

        if form.is_valid():

            dic = {
                "Receiver_Name": form.cleaned_data["receiverName"],
                "Receiver_Last_Name": form.cleaned_data["receiverLastName"],
                "Lending_Date": str(form.cleaned_data["lendingDate"]),
                "Return_Date": str(form.cleaned_data["returnDate"]),
                "Book_Name": form.cleaned_data["bookName"],
                "Book_ID": form.cleaned_data["bookid"],
                "Quantity": form.cleaned_data["quantity"],
            }


            # -------------------------
            # READ BOOKS
            # -------------------------
            try:
                with open("all_books.json", "r") as file:
                    allBooks = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):
                allBooks = []


            # -------------------------
            # FIND BOOK
            # -------------------------
            found = False

            for book in allBooks:

                if book["Book_ID"] == dic["Book_ID"]:

                    found = True

                    # subtract lending quantity
                    book["Quantity"] -= dic["Quantity"]

                    break


            # -------------------------
            # BOOK ID NOT FOUND
            # -------------------------
            if found == False:

                form.add_error(
                    "bookid",
                    "Book ID does not exist."
                )

                return render(
                    request,
                    "lendingBook.html",
                    {"form": form}
                )


            # -------------------------
            # SAVE UPDATED QUANTITY
            # -------------------------
            with open("all_books.json", "w") as file:
                json.dump(allBooks, file, indent=4)


            # -------------------------
            # READ LENDING DATA
            # -------------------------
            try:
                with open("lend.json", "r") as file:
                    allDataLend = json.load(file)

                if isinstance(allDataLend, dict):
                    allDataLend = [allDataLend]

            except (FileNotFoundError, json.JSONDecodeError):
                allDataLend = []


            # -------------------------
            # SAVE LENDING
            # -------------------------
            allDataLend.append(dic)

            with open("lend.json", "w") as file:
                json.dump(allDataLend, file, indent=4)


            return redirect("Prograss")


    else:
        form = LendingForm()


    return render(
        request,
        "lendingBook.html",
        {"form": form}
    )
def show_lendedBook(request):

    try:
        with open("lend.json", "r") as file:
            allDataLend = json.load(file)

        if isinstance(allDataLend, dict):
            allDataLend = [allDataLend]

    except (FileNotFoundError, json.JSONDecodeError):
        allDataLend = []

    return render(
        request,
        "Lendedbook.html",
        {
            "allData": allDataLend
        }
    )

def addMember(request):

    if request.method == "POST":

        form = Addmember(request.POST)

        if form.is_valid():

            dic = {
                "ID": str(form.cleaned_data["memberId"]),
                "Name": form.cleaned_data["memberName"],
                "email": form.cleaned_data["email"],
                "Phone_Number": form.cleaned_data["phoneNumber"],
            }

            try:
                with open("members.json", "r") as file:
                    allMembers = json.load(file)

                if isinstance(allMembers, dict):
                    allMembers = [allMembers]

            except (FileNotFoundError, json.JSONDecodeError):
                allMembers = []

            # Add new member
            allMembers.append(dic)

            # Save members back into JSON
            with open("members.json", "w") as file:
                json.dump(allMembers, file, indent=4)

          

    else:
        form = Addmember()

    return render(
        request,
        "addMember.html",
        {
            "form": form
        }
    )
def showMember(request):

    try:
        with open("members.json", "r") as file:
            showmember = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        showmember = []

    return render(
        request,
        "showMember.html",
        {
            "showmember": showmember
        }
    )
def  returnbook_search(request):
        with open("lend.json", "r") as file:
            allbookslend = json.load(file)
        return render(request,'returnbook.html',{'all':allbookslend})
    
def returnBook(request):

    form = ReturnForm()

    if request.method == "POST":

        form = ReturnForm(request.POST)

        if form.is_valid():

            book_id = form.cleaned_data["bookId"]
            book_name = form.cleaned_data["bookName"]


            # --------------------------------
            # 1. READ LENDED BOOKS
            # --------------------------------
            try:
                with open("lend.json", "r") as file:
                    allbookslend = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):
                allbookslend = []


            # --------------------------------
            # 2. SEARCH FOR LENDED BOOK
            # --------------------------------
            found = False
            returned_book = None

            for book in allbookslend:

                if (
                    book["Book_ID"] == book_id
                    and book["Book_Name"] == book_name
                ):

                    found = True
                    returned_book = book
                    break


            # --------------------------------
            # 3. IF NOT FOUND
            # --------------------------------
            if found == False:

                form.add_error(
                    "bookId",
                    "This book was not found in the lending list."
                )

                return render(
                    request,
                    "return.html",
                    {"form": form}
                )

            return redirect("returnbook_search")


    return render(
        request,
        "return.html",
        {
            "form": form
        }
    )

def return_remove_add(request, bookid):
    if request.method == 'POST':

        with open("lend.json", "r") as file:
            allbookslend = json.load(file)

        returned_book = None

        for i in allbookslend:
            if bookid == i["Book_ID"]:
                returned_book = i
                allbookslend.remove(i)
                break

        with open("lend.json", "w") as file:
            json.dump(allbookslend, file, indent=4)

        with open("all_books.json", "r") as file:
            allData = json.load(file)

        if returned_book:
            for book in allData:
                if bookid == book["Book_ID"]:
                    book["Quantity"] += returned_book["Quantity"]
                    break

        with open("all_books.json", "w") as file:
            json.dump(allData, file, indent=4)

        return redirect("returnbook_search")  
