from django.shortcuts import render, redirect, get_object_or_404  
from .forms import ReagentForm, ConsumableForm, ControlForm
from .models import Management, Question, Takeout
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    return render(request, 'index.html')


def reagent(request):
    page = request.GET.get('page', '1') 
    kw = request.GET.get('kw', '') 

    managements = Management.objects.order_by('-registration_date')
    if kw:
        managements = managements.filter(
            Q(product_name__icontains=kw) |  
            Q(storage_location__icontains=kw) | 
            Q(partname__icontains=kw) 
        ).distinct()
    
    paginator = Paginator(managements, 7)  
    page_obj = paginator.get_page(page)

    context = {'managements': page_obj, 'page': page, 'kw': kw}  

    return render(request, 'reagent.html', context)


def reagentcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ReagentForm(request.POST, request.FILES)
        if form.is_valid():
            management = form.save(commit=False)
            management.author = request.user
            management.save()
            return redirect('reagent')
    else:   
        form = ReagentForm()
    return render(request, 'reagent_form.html', {'form':form})    


def detail(request, management_id):
    management = get_object_or_404(Management, pk=management_id)
    return render(request, 'detail.html', {'management':management})

def consumables(request):
    page = request.GET.get('page', '1')  
    kw = request.GET.get('kw', '')  

   
    questions = Question.objects.order_by('-item_code')
    if kw:
        questions = questions.filter(
            Q(product_name__icontains=kw) |  
            Q(storage_location__icontains=kw) | 
            Q(team_name__icontains=kw) 
        ).distinct()
    paginator = Paginator(questions, 7)  
    page_obj = paginator.get_page(page)

    context = {'questions': page_obj, 'page': page, 'kw': kw} 
    return render(request, 'consumables.html', context)    

def consumablecreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ConsumableForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('consumables')
    else:   
        form = ConsumableForm()
    return render(request, 'consumables_form.html', {'form':form})     

def con_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'con_detail.html',{'question':question})  



def control(request):
    page = request.GET.get('page', '1')  
    kw = request.GET.get('kw', '') 

    takeouts = Takeout.objects.order_by('-carry_day')
    if kw:
        takeouts = takeouts.filter(
            Q(carry_team__icontains=kw) |  
            Q(receive_company__icontains=kw) |
            Q(material_name__icontains=kw)
        ).distinct()
    paginator = Paginator(takeouts, 7) 
    page_obj = paginator.get_page(page)

    context = {'takeouts': page_obj, 'page': page, 'kw': kw}  
    return render(request, 'control.html', context)     


def controlcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ControlForm(request.POST, request.FILES)
        if form.is_valid():
            takeout = form.save(commit=False)
            takeout.author = request.user
            takeout.save()
            return redirect('control')
    else:   
        form = ControlForm()
    return render(request, 'control_form.html', {'form':form}) 


def trol_detail(request, takeout_id):
    takeout = get_object_or_404(Takeout, pk=takeout_id)
    return render(request, 'trol_detail.html',{'takeout':takeout})      
    
@login_required(login_url='login')
def management_modify(request, management_id):
    """
    제품수정
    """
    management = get_object_or_404(Management, pk=management_id)
    if request.user != management.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('detail', management_id=management.id)

    if request.method == "POST":
        form = ReagentForm(request.POST, instance=management)
        if form.is_valid():
            management = form.save(commit=False)
            management.author = request.user
            management.save()
            return redirect('detail', management_id=management.id)
    else:
        form = ReagentForm(instance=management)
    context = {'form': form}
    return render(request, 'reagent_form.html', context)

@login_required(login_url='login')
def management_delete(request, management_id):
    """
   제품삭제
    """
    management = get_object_or_404(Management, pk=management_id)
    if request.user != management.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('detail', management_id=management.id)
    management.delete()
    return redirect('reagent')

@login_required(login_url='login')
def question_modify(request, question_id):
    """
    제품수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('con_detail', question_id=question.id)

    if request.method == "POST":
        form = ConsumableForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('con_detail', question_id=question.id)
    else:
        form = ConsumableForm(instance=question)
    context = {'form': form}
    return render(request, 'consumables_form.html', context)

@login_required(login_url='login')
def question_delete(request, question_id):
    """
   제품삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('con_detail', question_id=question.id)
    question.delete()
    return redirect('consumables')


@login_required(login_url='login')
def takeout_modify(request, takeout_id):
    """
    제품수정
    """
    takeout = get_object_or_404(Takeout, pk=takeout_id)
    if request.user != takeout.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('trol_detail', takeout_id=takeout.id)

    if request.method == "POST":
        form = ControlForm(request.POST, instance=takeout)
        if form.is_valid():
            takeout = form.save(commit=False)
            takeout.author = request.user
            takeout.save()
            return redirect('trol_detail', takeout_id=takeout.id)
    else:
        form = ControlForm(instance=takeout)
    context = {'form': form}
    return render(request, 'control_form.html', context)   


@login_required(login_url='login')
def takeout_delete(request, takeout_id):
    """
   제품삭제
    """
    takeout = get_object_or_404(Takeout, pk=takeout_id)
    if request.user != takeout.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('trol_detail', takeout_id=takeout.id)
    takeout.delete()
    return redirect('control')