from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def contacto(request):
    return render(request, 'contacto.html')

def localizacion(request):
    context = {
        'localizacion': {
            'direccion': 'Calle Alegre 88, Málaga, España',
            'latitud': 36.7213028,
            'longitud': -4.4216366,
        },
        'contacto': {
            'telefono': '+34 123 456 789',
            'email': 'info@fruteriaturing.com',
        }
    }
    return render(request, 'localizacion.html', context=context)
