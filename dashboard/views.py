from django.shortcuts import render, redirect

from .models import *
from .searializers import *
from pages.models import UserProfile

# Create your views here.

def dashHome(request):
    # print(request.user)
    transfers = Trans.objects.all()
    profile = UserProfile.objects.filter(user = request.user)
    ctxt = {
        'profile' : profile[0],
        'transfers' : transfers,
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

    print(str(bud))

    wbs = WBS.objects.filter(budget = bud)

    situation = 1

    transferWBS = []
    wbAll = []

    tr = Trans.objects.all()

    for w in wbs:
        wbAll.append(w)

    for i in tr:
        if i.wbs_item in wbAll:
            transferWBS.append(i)


    print(str(wbAll))
    print(str(transferWBS))


    ctxt = {
        'profile' : profile[0],
        'bud' : bud,
        'wbAll' : wbAll,
        'transferWBS' : transferWBS,
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

def comms(request, wbid):
    if request.method == 'POST':
        if 'comment' in request.POST:
            print("You have commented")
            return redirect('/dashboard/comments/'+str(wbid))
    else:
        profile = UserProfile.objects.filter(user = request.user)
        wbs = WBS.objects.filter(id = wbid)[0]

        try:
            comments = Comment.objects.filter(wbs_item = wbs)
        except:
            comments = []

        try:
            transfers = Trans.objects.filter(wbs_item = wbid)[0]
            type = transfers.type

            if(type is 1):
                t = 'Add'
            elif(type is 2):
                t = 'Remove'
            elif type is 3:
                t = 'Transfer'
        except:
            t = 'None'

        ctxt = {
            'profile' : profile[0],
            'wbs' : wbs,
            'transfer' : t,
            'comments' : comments,
        }
        return render(request, 'dashboard/comments.html', context=ctxt)

def elementAdd(request):

    profile = UserProfile.objects.filter(user = request.user)
    ccs = CostCenters.objects.all()
    ctxt = {
        'profile' : profile[0],
        'ccs' : ccs,
    }
    return render(request, 'dashboard/addWBS.html', context=ctxt)
