from django.shortcuts import render
from .forms import KonfiguratorForm
from .models import GalleryImage

def index(request):
    vysledna_cena = None
    if request.method == 'POST':
        form = KonfiguratorForm(request.POST)
        if form.is_valid():
            ram = form.cleaned_data['ram']
            vidlice = form.cleaned_data['vidlice']
            brzdy = form.cleaned_data['brzdy']
            prehazovacka = form.cleaned_data['prehazovacka']
            vysledna_cena = sum([
                ram.cena,
                vidlice.cena,
                brzdy.cena,
                prehazovacka.cena
            ])
    else:
        form = KonfiguratorForm()

    return render(request, 'bikes/index.html', {
        'form': form,
        'vysledna_cena': vysledna_cena
    })
def gallery_view(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'bikes/gallery.html', {'images': images})