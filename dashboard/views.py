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
            usr = request.POST['user']
            wbs = WBS.objects.filter(id = wbid)[0]
            text = request.POST['text']
            attachment = request.POST['attachment']

            comt = Comment()
            comt.user = request.user
            comt.wbs_item = wbs
            comt.text = text
            comt.attachment = attachment
            comt.save()

            type = int(request.POST['type'])

            if type > 0:
                transfer = Trans()
                transfer.wbs_item = wbs
                transfer.type = int(request.POST['type'])
                transfer.amount = float(request.POST['amount'])
                transfer.save()

            return redirect('/dashboard/comments/'+str(wbid))

        elif 'accept' in request.POST:
            usr = request.POST['user']
            wbs = WBS.objects.filter(id = wbid)[0]
            text = request.POST['text']
            attachment = request.POST['attachment']

            comt = Comment()
            comt.user = request.user
            comt.wbs_item = wbs
            comt.text = text
            comt.attachment = attachment
            comt.save()

            comt = Comment()
            comt.user = request.user
            comt.wbs_item = wbs
            comt.text = 'Transfer Accepted'
            # comt.attachment = attachment
            comt.save()

            transfers = Trans.objects.filter(wbs_item = wbid)

            tfs = []

            for t in transfers:
                tfs.append(t)
            transfers = tfs[-1]

            if(transfers.type == 1):
                wbs.amount = wbs.amount + transfers.amount
                wbs.save()
            elif(transfers.type == 2):
                wbs.amount = wbs.amount - transfers.amount
                wbs.save()
            elif(transfers.type == 3):
                t3 = TypeThree.objects.filter(trans=transfers)[-1]
                tfs = []

                for t in t3:
                    tfs.append(t)
                t3 = tfs[-1]

                targetWbs = WBS.objects.filter(id = (t3.transfer_target.id))
                targetWbs.amount = targetWbs.amount - transfers.amount
                wbs.amount = wbs.amount + transfers.amount
                wbs.save()
                targetWbs.save()
            transfers.status = False
            return redirect('/dashboard/comments/'+str(wbid))

        elif 'reject' in request.POST:
            transfers.status = False

            comt = Comment()
            comt.user = request.user
            comt.wbs_item = wbs
            comt.text = 'Transfer Rejected'
            # comt.attachment = attachment
            comt.save()
            return redirect('/dashboard/comments/'+str(wbid))

        return redirect('/dashboard/comments/'+str(wbid))
    else:
        profile = UserProfile.objects.filter(user = request.user)
        wbs = WBS.objects.filter(id = wbid)[0]

        try:
            comments = Comment.objects.filter(wbs_item = wbs)
        except:
            comments = []

        try:
            transfers = Trans.objects.filter(wbs_item = wbid)
            tfs = []
            for t in transfers:
                tfs.append(t)
            transfers = tfs[-1]
            
            if(transfers.status is True):
                type = transfers.type

                if(type is 1):
                    t = 'Add'
                elif(type is 2):
                    t = 'Remove'
                elif type is 3:
                    t = 'Transfer'
            else:
                t = None
        except:
            t = None

        print(str(comments))

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
