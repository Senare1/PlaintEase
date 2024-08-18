from django.shortcuts import render,redirect,get_object_or_404
from .forms import ComplaintForm,ProofForm
from .models import Complaint,Proof,Response
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

@login_required
def home(request):
    complainant = request.user
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    context = {
        'number': number_response
    }
    return render(request,"complaints/home.html",context)

@login_required
def response(request):
    complainant = request.user
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    responses = complainant.responses_complaints.all().exclude(status_deleted=True)
    context = {
        'responses': responses,
        'number': number_response
    }
    return render(request,"complaints/response.html",context)

@login_required
def help(request):
    complainant = request.user
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    context = {
        'number': number_response
    }
    return render(request,'complaints/help.html',context)

@login_required
def plaint_detail(request,id):
    complainant = request.user
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    complaint = get_object_or_404(complainant.complaints,id=id,complaint_deleted=True)
    proofs = complaint.proofs.all()
    context = {
        'complaint': complaint,
        'proofs': proofs,
        'number': number_response,
        }
    return render(request,'complaints/plaint_detail.html',context)

@login_required
def delete_response(request,id):
    complainant = request.user
    response = get_object_or_404(complainant.responses_complaints,id=id,status_deleted=False)
    response.status_deleted=True
    response.save()
    previous_page = request.META.get('HTTP_REFERER')
    if previous_page:
        return redirect(previous_page)
    else:
        return redirect('response')

@login_required
def delete_plaint(request,id):
    complainant = request.user
    complaint = get_object_or_404(complainant.complaints,id=id)

    if complaint.status != "running":
        complaint.complaint_delete=True
        complaint.save()
    previous_page = request.META.get('HTTP_REFERER')
    if previous_page:
        return redirect(previous_page)
    else:
         return redirect('home')

@login_required
def my_plaints(request):
    complainant = request.user
    number_complaint = complainant.complaints.all().filter(complaint_delete=False).count()
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    plaints = complainant.complaints.all().exclude(complaint_delete=True)
    context = {
        'number': number_response,
        'complaints': plaints,
        'number_complaint': number_complaint,
    }
    return render(request,"complaints/etat.html",context)


@login_required
def let_plaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.complainant = request.user
            form.save()
            send_mail(
                "PlaintEase.com",
                f"Salut M(r) {request.user} ,nous accusons reception de votre plainte.Nous vous reviendrons.Merci à bientot",
                'arsenenikiema685@gmail.com',
                [request.user.email],
                fail_silently=False,
            )
            return redirect('proof_data')
        else:
            form.add_error(None,'Non autorisés')
    else:
        form = ComplaintForm()
    complainant = request.user
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    context = {
        'form': form,
        'number': number_response,
    }
    return render(request,'complaints/formulaire.html',context)


@login_required
def proof_data(request):
    if request.method == 'POST':
        form = ProofForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            complainant = request.user
            complaint = complainant.complaints.all().last()
            if not complaint:
                return redirect('not_found_404')

            form.proof_complaint = complaint
            form.save()
            return redirect('my_plaints')
    else:
        form = ProofForm()
    complainant = request.user
    number_response = complainant.responses_complaints.all().exclude(status_deleted=True).count()
    context = {
        'form': form,
        'number': number_response,
    }
    return render(request,'complaints/preuves.html',context)


