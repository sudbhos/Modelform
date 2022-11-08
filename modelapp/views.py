from django.shortcuts import render
from . import forms
# Create your views here.
def StudentViews(request,):
    form=forms.studentdetails()
    if request.method=="POST":
        form=forms.studentdetails(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data uploaded successfully ..")
    return render(request,"testapp/index.html",{"form":form})
