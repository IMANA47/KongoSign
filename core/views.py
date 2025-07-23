from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

@login_required
def dashboard_redirect(request):
    user = request.user
    if user.is_admin():
        return redirect('admin_dashboard')
    elif user.is_client():
        return redirect('client_dashboard')
    elif user.is_signataire():
        return redirect('signataire_dashboard')
    else:
        return redirect('login')


@login_required
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def client_dashboard(request):
    return render(request, 'core/client_dashboard.html')

@login_required
def signataire_dashboard(request):
    return render(request, 'core/signataire_dashboard.html')

@login_required
def client_dashboard(request):
    documents = Document.objects.filter(owner=request.user, is_archived=False)
    signataires = CustomUser.objects.filter(role='SIGNATAIRE')

    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.owner = request.user
            doc.save()
            return redirect('client_dashboard')
    else:
        form = DocumentUploadForm()

    return render(request, 'core/client_dashboard.html', {
        'documents': documents,
        'form': form,
        'signataires': signataires
    })


@login_required
def share_document(request):
    if request.method == 'POST':
        form = DocumentShareForm(request.POST)
        if form.is_valid():
            document = get_object_or_404(Document, id=form.cleaned_data['document_id'], owner=request.user)
            signataire = form.cleaned_data['signataire']

            # Empêche le partage en double
            if not DocumentShare.objects.filter(document=document, signataire=signataire).exists():
                DocumentShare.objects.create(document=document, signataire=signataire)
        return redirect('client_dashboard')

@login_required
def signataire_dashboard(request):
    shares = DocumentShare.objects.filter(signataire=request.user, document__is_archived=False)
    return render(request, 'core/signataire_dashboard.html', {
        'shares': shares
    })
