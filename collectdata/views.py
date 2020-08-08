from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,HttpResponse,get_object_or_404
from django.contrib import messages
# Create your views here.
from .forms import NewUserForm
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'collectdata/login.html',{"form":form})

@login_required(login_url='login')
def home(request):
    cust=UserDetail.objects.all()
    total=Basicdata.objects.all()
    total_data=total.count()
    return render(request,'collectdata/home.html',{'cust':cust,'total_data':total_data})

@login_required(login_url='login')
def Details(request):
    if request.method == 'POST':
        post=UserDetail()
        post.name= request.POST.get('name')
        post.save()
        return redirect('add_form')
    return render(request,'collectdata/details.html')
    
@login_required(login_url='login')
def add_form(request):
    re=UserDetail.objects.all()
    if request.method == 'POST':
        basic=('date') and ('stime') and ('ftime') and ('totaltime') and ('firstperception') and ('lastperception') and ('td') and ('correct') and ('displaced') and ('total_meld') and ('correct_meld') and ('incorrect_meld') and ('type') and ('C180body') and ('opposition') and ('bracketediror') and ('giantsquare') and ('house')
        boo=('boostanglebody') and ('babody') and ('badegree') and ('badegreetype')
        boost=('boostanglebody') and ('bbody') and ('boostsymbol') and ('bbody') and ('bdegree') and ('bdegreetype') and ('benergy')
        cond=('conditionbody') and ('condition1') and ('cdegree') and ('cdegreetype') and ('cenergy')
        ir=('irbody') and ('irdegree') and ('irdt') and ('irbody1') and ('irenergy')
        gas=('gastype') and ('gdegree') and ('gassymbol')and ('gdegreetype') and ('genergy')
        c=('C90body') and ('C90symbol') and ('C90body1') and ('C90degree')  and ('C90degreetype')
        opp=("oppbody1") and ('oppositiondeg') and ('oppbody2') and ("oppdegree") and ("oppdegreetype")
        sextile=('sextilebody') and('sextilesymbol') and ('sextilebody1') and ('sextiledegree') and ('sextiledegreetype')
        trine=('trinesymbol') and ('trinebody') and ("trinebody1") and ('trinedegree') and ('trinedegreetype')
        bracketedC=('bracketedCbody') and ('bracketedsymbol') and ('bracketedCbody1') and ('bracketeddegree') and ('brackedteddegreetype')
        multiple=('multiplebody') and ('multiplesymbol') and ("multiplebody1") and ('multipledegree') and ('multipledegreetype')
        moon =('moonsym') and ('moonbody') and ('moondegree') and ('moondegreetype')
        bracket=("bracket") and ("bracketbody") and ("bracketdegree")
        if request.POST.get(basic) and (boo) and (boost) and (cond) and (ir) and (gas) and (c) and (opp) and (sextile) and (trine) and (moon) and (bracketedC) and (multiple):
            name= region=request.POST['name']
            post=Basicdata()
            post.name= UserDetail.objects.get(pk=name)
            post.date= request.POST.get('date')
            post.start_time= request.POST.get('stime')
            post.stop_time=request.POST.get('ftime')
            post.total_time=request.POST.get('totaltime')
            post.first_perception=request.POST.get('firstperception')
            post.last_perception=request.POST.get('lastperception')
            post.total_drawing= request.POST.get('td')
            post.correct=request.POST.get('correct')
            post.displaced=request.POST.get('displaced')
            post.total_meld=request.POST.get('total_meld')
            post.correct_meld=request.POST.get('correct_meld')
            post.incorect_meld=request.POST.get('incorrect_meld')
            post.type=request.POST.get('type')
            post.opp=request.POST.get('C180body')
            post.multiple_opposition=request.POST.get('opposition')
            post.bracketedIROR=request.POST.get('bracketediror')
            post.giantsquare=request.POST.get('giantsquare')
            post.house=request.POST.get('house')
            post.save()
            
            
            banglebody=request.POST.getlist('boostanglebody')
            bbody0=request.POST.getlist('babody')
            bdegtype0=request.POST.getlist('badegreetype')
            bdegree0=request.POST.getlist('badegree')
            bbody0_data=len(bbody0)
            for i in range(bbody0_data):
                post1=BoostAngle()          
                post1.name=UserDetail.objects.get(pk=name)
                post1.boostanglebody=banglebody[i]
                post1.body=bbody0[i]
                post1.degree=bdegtype0[i]
                post1.degree_type=bdegree0[i]
                post1.save()
                
            banglebody=request.POST.getlist('boostanglebody1')
            bbody0=request.POST.getlist('bbody')
            bangle0=request.POST.getlist('boostsymbol')
            bbody00=request.POST.getlist('bbody')
            bdegtype0=request.POST.getlist('bdegreetype')
            bdegree0=request.POST.getlist('bdegree')
            beng0=request.POST.getlist('benergy')
            bbody0_data=len(bbody0)
            for i in range(bbody0_data):
                post2=BoostAngleDetail()          
                post2.name=UserDetail.objects.get(pk=name)
                post2.boostanglebody=banglebody[i]
                post2.body=bbody0[i]
                post2.boost_symbol=bangle0[i]
                post2.body1= bbody00[i]
                post2.degree=bdegtype0[i]
                post2.degree_type=bdegree0[i]
                post2.energy=beng0[i]
                post2.save()

                
            condbody=request.POST.getlist('conditionbody')
            cond1=request.POST.getlist('condition1')
            deg=request.POST.getlist('cdegree')
            degtype=request.POST.getlist('cdegreetype')
            cener= request.POST.getlist('cenergy')
            all_data=len(cond1)
            for i in range(all_data):
                post3=Condition()          
                post3.name=UserDetail.objects.get(pk=name)
                post3.conditionbody=condbody[i]
                post3.first_condition=cond1[i]
                post3.degree=deg[i]
                post3.degree_type=degtype[i]
                post3.energy=cener[i]                
                post3.save() 
            
            irbody=request.POST.getlist('irbody')
            irdeg=request.POST.getlist('irdegree')
            irsym=request.POST.getlist('irsymbol')
            irdegtype=request.POST.getlist('irdegreetype')
            irbody1=request.POST.getlist('irbody1')
            irene=request.POST.getlist('irenergy')
            ir_data=len(irbody)
            for i in range(ir_data):
                post4=Irsupport()
                post4.name=UserDetail.objects.get(pk=name)
                post4.body=irbody[i]
                post4.degree=irdeg[i]
                post4.sym=irsym[i]
                post4.degree_type=irdegtype[i] 
                post4.body1=irbody1[i]
                post4.energy=irene[i]              
                post4.save()
                 
            
            ggas=request.POST.getlist('gastype')
            gbody=request.POST.getlist('gbody')
            gsymbol=request.POST.getlist('gasymbol')
            gdegree=request.POST.getlist('gdegree')
            gdegtype=request.POST.getlist('gdegreetype')
            genergy=request.POST.getlist('genergy')
            gas_data=len(gbody) 
            for i in range(gas_data):    
                post5=Gasgiant()
                post5.name=UserDetail.objects.get(pk=name)
                post5.gas=ggas[i]
                post5.symbol=gsymbol[i]
                post5.body=gbody[i]
                post5.degree=gdegree[i]
                post5.degree_type=gdegtype[i]
                post5.energy=genergy[i]  
                post5.save()
            
            c90body= request.POST.getlist('C90body')
            c90symbol=request.POST.getlist('C90symbol')
            c90body1=request.POST.getlist('C90body1')
            c90a=request.POST.getlist('C90degree')
            c90s=request.POST.getlist('C90degreetype')
            c90_data=len(c90body)
            for i in range(c90_data):    
                post6=C()
                post6.name=UserDetail.objects.get(pk=name)
                post6.body=c90body[i]
                post6.symbol=c90symbol[i]
                post6.body1=c90body1[i]
                post6.degree=c90a[i]
                post6.degree_type=c90s[i]  
                post6.save()
                
            opbody1=request.POST.getlist('oppbody1')
            opdeg=request.POST.getlist('oppositiondeg')
            opbody2=request.POST.getlist('oppbody2')
            opa=request.POST.getlist('oppdegree')
            ops=request.POST.getlist('oppdegreetype')
            opp_data=len(opbody1)
            for i in range(opp_data):    
                post7=Opposition()
                post7.name=UserDetail.objects.get(pk=name)
                post7.body1=opbody1[i]
                post7.symbol=opdeg[i]
                post7.body2=opbody2[i]
                post7.degree=opa[i]
                post7.degree_type=ops[i]
                post7.save()
                
            sxbody=request.POST.getlist('sextilebody')
            sxsymbol=request.POST.getlist('sextilesymbol')
            sxbody1=request.POST.getlist('sextilebody1')
            sxa=request.POST.getlist('sextiledegree')
            sxs=request.POST.getlist('sextiledegreetype')
            sx_data=len(sxbody)
            for i in range(sx_data):    
                post8=Sextile()
                post8.name=UserDetail.objects.get(pk=name)
                post8.body=sxbody[i]
                post8.symbol=sxsymbol[i]
                post8.body1=sxbody1[i]
                post8.degree=sxa[i]
                post8.degree_type=sxs[i]
                post8.save()
            tbody=request.POST.getlist('trinebody')
            tsymbol=request.POST.getlist('trinesymbol')
            tbody1=request.POST.getlist('trinebody1')
            ta=request.POST.getlist('trinedegree')
            ts=request.POST.getlist('trinedegreetype')
            t_data=len(tbody)
            for i in range(t_data):    
                post9=Trine()
                post9.name=UserDetail.objects.get(pk=name)
                post9.body=tbody[i]
                post9.symbol=tsymbol[i]
                post9.body1=tbody1[i]
                post9.degree=ta[i]
                post9.degree_type=ts[i]
                post9.save()
                
            brbody=request.POST.getlist('bracketedCbody')
            brdeg90=request.POST.getlist('bracketedsymbol')
            brbody1=request.POST.getlist('bracketedCbody1')
            brapp=request.POST.getlist('bracketeddegree')
            brs=request.POST.getlist('brackedteddegreetype')
            br_data=len(brbody)
            for i in range(br_data):    
                post10=BracketedC()
                post10.name=UserDetail.objects.get(pk=name)
                post10.body=brbody[i]
                post10.symbol=brdeg90[i]
                post10.body1=brbody1[i]
                post10.degree=brapp[i]
                post10.degree_type=brs[i]
                post10.save()
            
            mulbody=request.POST.getlist('multiplebody')
            muldeg=request.POST.getlist('multiplesymbol')
            mulbody1=request.POST.getlist('multiplebody1')
            mulap=request.POST.getlist('multipledegree')
            mulsep=request.POST.getlist('multipledegreetype')
            mul_data=len(mulbody)
            for i in range(mul_data):    
                post11=MultipleSquare()
                post11.name=UserDetail.objects.get(pk=name)
                post11.body=mulbody[i]
                post11.symbol=muldeg[i]
                post11.body1=mulbody1[i]
                post11.degree=mulap[i]
                post11.degree_type=mulsep[i]
                post11.save()
                
            moonsym=request.POST.getlist('moonsym')
            moonbody=request.POST.getlist('moonbody')
            moondeg=request.POST.getlist('moondegree')
            moondegtype=request.POST.getlist('moondegreetype')
            moon_data=len(moonbody)
            for i in range(moon_data):
                post12=Moon()
                post12.name=UserDetail.objects.get(pk=name)
                post12.sym= moonsym[i]
                post12.body= moonbody[i]
                post12.degree=moondeg[i]
                post12.degree_type=moondegtype[i]
                post12.save()
            
            bracketed=request.POST.getlist('bracket')
            bracket_body=request.POST.getlist('bracketbody')
            bdegree_type=request.POST.getlist('bracketdegree')
            b_data=len(bracket_body)
            for i in range(b_data):
                post13=Bracketed()
                post13.name=UserDetail.objects.get(pk=name)
                post13.bracket=bracketed[i]
                post13.body=bracket_body[i]
                post13.degree_type=bdegree_type[i]            
                post13.save() 
            return redirect('/') 
    return render(request,'collectdata/form.html',{"re":re})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")