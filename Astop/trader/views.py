import q
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
from .forms import TraderForm, LoginForm, TraderEditForm
from .models import Trader
from django.contrib.auth.hashers import make_password
from manager.models import Client
from django.db.models import Q

# Create views.

def index(request):
    return render(request, 'index.html')


def plumber(request):
    plumbers = Client.objects.filter(occupation = 'Plumber')
    return render(request, 'plumber.html', {'plumbers': plumbers})

#electrician page
def electrician(request):
    #find all clients with occupation as electrician
    electricians = Client.objects.filter(occupation='Electrician')
    return render(request, 'electrician.html', {'electricians': electricians})


def handyman(request):
    handymen = Client.objects.filter(occupation='Handyman')
    return render(request, 'handyman.html', {'handymen': handymen})



def details(request, client_id):
    client = Client.objects.get(client_id=client_id)

    trader = None
    if request.session.get('trader_id'):
        try:
            trader = Trader.objects.get(id = request.session['trader_id'])
        except Trader.DoesNotExist:
            trader = None
    return render(request, 'details.html', {'client': client, 'trader': trader})

# register trader promo details
@require_http_methods(['GET', 'POST'])
def registration(request):
    if request.method == 'GET':
        form = TraderForm()
        return render(request, 'registration.html', {'form': form})
    else:
        form = TraderForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['password']:
                form.add_error('password', 'Password is required')
                return render(request, 'registration.html', {'form': form})
            else:
                client_id_value = form.cleaned_data.get('client_id')
                password = make_password(form .cleaned_data.get('password'))
                email = form.cleaned_data.get('email')
                phone_number = form.cleaned_data.get('phone_number')

                try:
                    client = Client.objects.get(client_id=client_id_value)
                except Client.DoesNotExist:
                    form.add_error('client_id', 'Client ID not found')
                    return render(request, 'registration.html',{'form': form})

            Trader.objects.create(client_id=client, password=password, email=email, phone_number=phone_number)
            return redirect('trader:login')

        else:
            return render(request, 'registration.html', {'form': form})
#trader login
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': LoginForm()})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = Trader.objects.filter(email=email).first()

            if user and check_password(password, user.password):
                request.session['trader_id'] = user.id
                request.session['client_id'] = user.client_id.client_id
                return redirect('trader:promo_edit', client_id=user.client_id.client_id)
            else:
                form.add_error('email', 'Invalid email or password')
                return render(request, 'login.html', {'form': form})
        else:

            return render(request, 'login.html', {'form': form})

@require_http_methods(['GET', 'POST'])
def promo_edit(request,client_id):

    client = Client.objects.get(client_id=client_id)
    trader = Trader.objects.get(client_id=client_id)
    if request.method == 'GET':
        return render(request, 'promo_edit.html',
                      {'form':TraderEditForm(),
                       'trader':trader,
                       'client':client})
    else:

        form = TraderEditForm(request.POST,request.FILES,instance=trader)
        if form.is_valid():

            # trader.about_myself = form.cleaned_data.get('about_myself')
            # trader.promo_title = form.cleaned_data.get('promo_title')
            # trader.promo_content1 = form.cleaned_data.get('promo_content1')
            # trader.promo_content2 = form.cleaned_data.get('promo_content2')
            # trader.promo_content3 = form.cleaned_data.get('promo_content3')
            # trader.phone_number = form.cleaned_data.get('phone_number')
            # trader.email = form.cleaned_data.get('email')
            # trader.password = make_password(form .cleaned_data.get('password'))
            # trader.photo = form.cleaned_data.get('photo')
            # trader.promo_image = form.cleaned_data.get('promo_image')
            trader = form.save(commit=False)
            if form.cleaned_data['password']:
                trader.password = make_password(form.cleaned_data.get('password'))
            trader.save()
            return redirect('trader:details', client_id=client.client_id)
        else:
            return render(request, 'promo_edit.html', {'form': form, 'trader': trader, 'client':client})

@require_GET
def search(request):
    q = request.GET.get('q')

    client = Client.objects.filter(Q(first_name__icontains =q)|
                                   Q(last_name__icontains = q)|
                                   Q(city__icontains = q)|
                                    Q(occupation__icontains = q)|
                                    Q(trade_name__icontains = q)).order_by('client_id')

    return render(request, 'list.html', context={'clients':client})

def test(request):
    return render(request, 'test.html')



