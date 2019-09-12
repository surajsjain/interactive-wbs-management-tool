from django.shortcuts import render, redirect

from .models import *
from .searializers import *
from pages.models import UserProfile

# Create your views here.

def dashHome(request):
    # print(request.user)
    profile = UserProfile.objects.filter(user = request.user)
    ctxt = {
        'profile' : profile[0],
    }

    return render(request, 'dashboard/dashHome.html', context=ctxt)

def budgetDisp(request):
    # print(request.user)
    profile = UserProfile.objects.filter(user = request.user)

    buds = Budget.objects.all()

    ctxt = {
        'profile' : profile[0],
        'budgets' : buds,
    }

    return render(request, 'dashboard/allBudgets.html', context=ctxt)

def wbsDisp(request, budgetID):

    # print(request.user)
    profile = UserProfile.objects.filter(user = request.user)

    bud = Budget.objects.filter(id = budgetID)[0]

    wbs = WBS.objects.filter(budget = bud)
    transfers = Transfer.objects.filter(wbs_item = wbs)

    situation = 0
    wbsWithoutTransfers = wbs
    wbsWithTransfers = []

    if(len(teansfers) > 0):
        situation = 1
        wbsWithoutTransfers = []

        for t in transfers:
            wbsWithTransfers.append(t.wbs_item)

        for w in wbs:
            if w not in wbsWithTransfers:
                wbsWithoutTransfers.append(w)

    ctxt = {
        'profile' : profile[0],
        'bud' : bud,
        'situation' : situation,
        'wbsWithoutTransfers' : wbsWithoutTransfers,
        'transfers' : wbsWithTransfers
    }

    return render(request, 'dashboard/specificWBS.html', context=ctxt)

def budgetAdd(request):
    profile = UserProfile.objects.filter(user = request.user)
    if request.method == 'POST':

        # print(str(request.POST['product']))
        # print(str(request.POST['year']))
        # print(str(request.POST['quarter']))
        # print(str(request.POST['type']))

        b = Budget()
        b.year = request.POST['year']
        b.quarter = request.POST['quarter']
        b.type = request.POST['type']
        b.product = request.POST['product']
        b.save()

        return redirect('budgetPage')
    else:
        ctxt = {
            'profile' : profile[0],
        }
        return render(request, 'dashboard/addBudget.html', context=ctxt)

def wbsSpecificDisp(request):
    pass
