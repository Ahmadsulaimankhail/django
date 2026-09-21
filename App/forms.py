from django import forms


class Entry(forms.Form):

    bookId = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Book ID",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    bookName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Book Name",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    author = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Book Author",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    releaseDate = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    publisher = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Book Publisher",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "City",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    quantity = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Quantity",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "placeholder": "Book Description",
            "rows": 5,
            "class": "w-full border border-gray-300 rounded-lg px-4 py-3 resize-none"
        })
    )

    image = forms.ImageField(
        label="",
        widget=forms.ClearableFileInput(attrs={
            "accept": "image/*",
            "class": "hidden",
        })
    )
    category = forms.ChoiceField(
    label="",
    choices=[
        ("", "Select Category"),
        ("fiction", "Fiction"),
        ("history", "History"),
        ("science", "Science"),
        ("technology", "Technology"),
        ("religion", "Religion"),
        ("business", "Business"),
        ("other", "Other"),
    ],
    widget=forms.Select(attrs={
        "class": "w-full border border-gray-300 rounded-lg px-4 py-3 outline-none focus:border-[#006d8b]"
    }))
    email = forms.EmailField(
            label="",
            widget=forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "border border-gray-300 rounded-lg px-4 py-3"
            })
        )
    phoneNumber = forms.IntegerField(
            label="",
            widget=forms.NumberInput(attrs={
                "placeholder": "Phone Number",
                "class": "border border-gray-300 rounded-lg px-4 py-3"
            })
        )
    

class LendingForm(forms.Form):

    receiverName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Receiver First Name",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    receiverLastName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Receiver Last Name",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    lendingDate = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    returnDate = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    bookName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Book Name",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    bookid = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Book ID",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    quantity = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Quantity",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )


class Addmember(forms.Form):

    memberId = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Member ID",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    memberName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Member Name",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

    phoneNumber = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Phone Number",
            "class": "border border-gray-300 rounded-lg px-4 py-3"
        })
    )

class ReturnForm(forms.Form):

    bookId = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter Book ID",
            "class": """
                w-full border border-gray-300 rounded-lg
                px-4 py-3 outline-none
                focus:border-[#006d8b]
                focus:ring-1 focus:ring-[#006d8b]
                transition
            """
        })
    )

    bookName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter Book Name",
            "class": """
                w-full border border-gray-300 rounded-lg
                px-4 py-3 outline-none
                focus:border-[#006d8b]
                focus:ring-1 focus:ring-[#006d8b]
                transition
            """
        })
    )