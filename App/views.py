from django.shortcuts import render, redirect
from .forms import Entry, LendingForm, Addmember, ReturnForm
import json
import os


# Vercel writable temporary storage
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