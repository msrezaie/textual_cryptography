# Import the required modules
from django.shortcuts import render, redirect
from . models import Project, Profile, Page
from . forms import ContactForm

# Define the view function
def base(request):
    # Get the first Page object from the database
    page = Page.objects.first()
    # Get the first Profile object from the database
    profile = Profile.objects.first()
    # Get all Project objects from the database
    projects = Project.objects.all()

    # Create a ContactForm object with data from the request (if it is a POST request)
    form = ContactForm(request.POST or None)
    # Initialize a form_message variable
    form_message = ""

    # Check if the request method is POST and the form data is valid
    if request.method == 'POST' and form.is_valid():
        # Save the form data to the database
        form.save()
        # Set the form_message variable to a success message
        form_message = "Thank you for contacting, I will get back to you ASAP!"

    # Create a context dictionary to pass data to the template
    context = {
        'profile': profile,
        'projects': projects,
        'page': page,
        'form': form,
        'form_message': form_message,
    }
    
    # Render the template with the context data and return it as the response
    return render(request, "base/base.html", context)

