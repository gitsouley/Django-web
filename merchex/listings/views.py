from django.shortcuts import redirect, render
from django.http import HttpResponse
from listings.models import Band
from listings.forms import ContactForm
from django.core.mail import send_mail
from listings.forms import BandForm


def vue(request):
    return render(request, 'listings/vue.html')

def band_list(request):
    bands = Band.objects.all()
    return render(request,'listings/band_list.html', {'bands' : bands})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'bandCreate': form})


def update_band(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band_detail', band.id)
    else:
        form = BandForm(instance=band) # créer un formulaire pré-rempli avec les données du groupe que nous voulons mettre à jour
    return render(request, 'listings/band_update.html', {'form': form})


def delete_band(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band_list')
    return render(request, 'listings/band_delete.html', {'band': band})


def about(request):
    print("la methode est appelée : ", request.method)
    print("le contenu du formulaire est : ", request.POST)
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('sent_email')  # redirige vers la même page pour afficher un formulaire vide après l'envoi du message
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactForm()
    return render(request, 'listings/about.html', {'contact': form})

def band_details(request, id):
    band = Band.objects.get(id=id)
    return render(request,'listings/band_detail.html', {'band': band})