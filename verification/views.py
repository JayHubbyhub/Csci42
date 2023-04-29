from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadForm
from .models import Verification
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
def verification(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            verform = form.save(commit=False)
            verform.username = request.user
            verform.save()
            return render(request, 'verificationform.html', {'form': form, 'message': 'Form successfully submitted.'})
        else:
            return render(request, 'verificationform.html', {'form': form, 'message': 'Form is invalid.'})
    else:
        form = UploadForm()
        form.fields['username'].queryset = User.objects.filter(username=request.user.username)
        return render(request, 'verificationform.html', {'form': form})

def displayVerForms(request):
    all_verforms = Verification.objects.filter(isChecked=False)
    return render(request, 'displayverforms.html', {'all_verforms': all_verforms})

def updateStatus(request, pk, new_status):
    # get the object
    obj = get_object_or_404(Verification, pk=pk)
    # update the status field
    obj.status = new_status
    obj.isChecked = True;
    obj.save()
    # render a response
    return redirect('verification:displayverforms')