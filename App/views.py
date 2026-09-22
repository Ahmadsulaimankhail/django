from django.shortcuts import render, redirect
from .forms import Entry, LendingForm, Addmember, ReturnForm
import json


# Vercel temporary writable folder
BASE_PATH = "/tmp/"



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

                with open(BASE_PATH + "new.json", "r") as file:

                    allData = json.load(file)


                if isinstance(allData, dict):

                    allData = [allData]


            except (FileNotFoundError, json.JSONDecodeError):

                allData = []



            allData.append(dic)



            with open(BASE_PATH + "new.json", "w") as file:

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

        with open(BASE_PATH + "all_books.json", "r") as file:

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

def edit_book(request, book_id):

    try:

        with open(BASE_PATH + "new.json", "r") as file:

            users = json.load(file)


    except (FileNotFoundError, json.JSONDecodeError):

        users = []



    user = next(
        (
            user for user in users
            if str(user["Book_ID"]) == str(book_id)
        ),
        None
    )



    if user is None:

        return redirect("Prograss")



    if request.method == "POST":

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



        if request.FILES.get("image"):

            image = request.FILES["image"]

            user["Image"] = image.name



        with open(BASE_PATH + "new.json", "w") as file:

            json.dump(users, file, indent=4)



        return redirect("ProGrass")



    return render(
        request,
        "editform.html",
        {
            "user": user
        }
    )

# =========================
# DELETE BOOK
# =========================

def delete_book(request, book_id):

    if request.method == "POST":

        try:

            with open(BASE_PATH + "new.json", "r") as file:

                allData = json.load(file)


        except (FileNotFoundError, json.JSONDecodeError):

            allData = []



        for i in allData:

            if str(book_id) == str(i["Book_ID"]):

                allData.remove(i)

                break



        with open(BASE_PATH + "new.json", "w") as file:

            json.dump(allData, file, indent=4)



    return redirect("Prograss")





# =========================
# LENDING BOOK
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



            try:

                with open(BASE_PATH + "all_books.json", "r") as file:

                    allBooks = json.load(file)



            except (FileNotFoundError, json.JSONDecodeError):

                allBooks = []




            found = False



            for book in allBooks:


                if str(book["Book_ID"]) == str(dic["Book_ID"]):

                    found = True

                    book["Quantity"] -= dic["Quantity"]

                    break





            if found == False:


                form.add_error(
                    "bookid",
                    "Book ID does not exist."
                )


                return render(
                    request,
                    "lendingBook.html",
                    {
                        "form": form
                    }
                )





            with open(BASE_PATH + "all_books.json", "w") as file:

                json.dump(
                    allBooks,
                    file,
                    indent=4
                )





            try:

                with open(BASE_PATH + "lend.json", "r") as file:

                    allDataLend = json.load(file)



                if isinstance(allDataLend, dict):

                    allDataLend = [allDataLend]


            except (FileNotFoundError, json.JSONDecodeError):

                allDataLend = []





            allDataLend.append(dic)





            with open(BASE_PATH + "lend.json", "w") as file:

                json.dump(
                    allDataLend,
                    file,
                    indent=4
                )



            return redirect("Prograss")



    else:

        form = LendingForm()



    return render(
        request,
        "lendingBook.html",
        {
            "form": form
        }
    )





# =========================
# SHOW LENDED BOOK
# =========================

def show_lendedBook(request):

    try:

        with open(BASE_PATH + "lend.json", "r") as file:

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





# =========================
# ADD MEMBER
# =========================

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

                with open(BASE_PATH + "members.json", "r") as file:

                    allMembers = json.load(file)



                if isinstance(allMembers, dict):

                    allMembers = [allMembers]


            except (FileNotFoundError, json.JSONDecodeError):

                allMembers = []





            allMembers.append(dic)





            with open(BASE_PATH + "members.json", "w") as file:

                json.dump(
                    allMembers,
                    file,
                    indent=4
                )



            return redirect("showMember")



    else:

        form = Addmember()



    return render(
        request,
        "addMember.html",
        {
            "form": form
        }
    )
# =========================
# SHOW MEMBERS
# =========================

def showMember(request):

    try:

        with open(BASE_PATH + "members.json", "r") as file:

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





# =========================
# RETURN BOOK SEARCH
# =========================

def returnbook_search(request):

    try:

        with open(BASE_PATH + "lend.json", "r") as file:

            allbookslend = json.load(file)


    except (FileNotFoundError, json.JSONDecodeError):

        allbookslend = []



    return render(
        request,
        "returnbook.html",
        {
            "all": allbookslend
        }
    )





# =========================
# RETURN BOOK
# =========================

def returnBook(request):

    form = ReturnForm()



    if request.method == "POST":

        form = ReturnForm(request.POST)



        if form.is_valid():

            book_id = form.cleaned_data["bookId"]

            book_name = form.cleaned_data["bookName"]



            try:

                with open(BASE_PATH + "lend.json", "r") as file:

                    allbookslend = json.load(file)


            except (FileNotFoundError, json.JSONDecodeError):

                allbookslend = []




            found = False

            returned_book = None




            for book in allbookslend:


                if (
                    str(book["Book_ID"]) == str(book_id)
                    and book["Book_Name"] == book_name
                ):

                    found = True

                    returned_book = book

                    break





            if found == False:


                form.add_error(
                    "bookId",
                    "This book was not found in the lending list."
                )



                return render(
                    request,
                    "return.html",
                    {
                        "form": form
                    }
                )



            return redirect("returnbook_search")



    return render(
        request,
        "return.html",
        {
            "form": form
        }
    )





# =========================
# REMOVE RETURNED BOOK
# ADD QUANTITY BACK
# =========================

def return_remove_add(request, bookid):

    if request.method == "POST":


        try:

            with open(BASE_PATH + "lend.json", "r") as file:

                allbookslend = json.load(file)



        except (FileNotFoundError, json.JSONDecodeError):

            allbookslend = []




        returned_book = None




        for i in allbookslend:


            if str(bookid) == str(i["Book_ID"]):

                returned_book = i

                allbookslend.remove(i)

                break





        with open(BASE_PATH + "lend.json", "w") as file:

            json.dump(
                allbookslend,
                file,
                indent=4
            )





        try:

            with open(BASE_PATH + "all_books.json", "r") as file:

                allData = json.load(file)



        except (FileNotFoundError, json.JSONDecodeError):

            allData = []





        if returned_book:


            for book in allData:


                if str(bookid) == str(book["Book_ID"]):

                    book["Quantity"] += returned_book["Quantity"]

                    break





        with open(BASE_PATH + "all_books.json", "w") as file:

            json.dump(
                allData,
                file,
                indent=4
            )



        return redirect("returnbook_search")
    