from django.shortcuts import redirect, render

from django.views.generic import FormView

from .models import ContactMessage

from .forms import ContactForm

# Create your views here.


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.save()
        # Todo: send email to message writer

        return redirect("success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = "success"

    def form_valid(self, form):
        message = form.save(commit=False)
        message.save()
        # Todo: send email to message writer
        return super().form_valid(form)
