from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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
