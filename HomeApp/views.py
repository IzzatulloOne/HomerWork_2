from django.shortcuts import render, redirect
from .models import Brand, Color, Car
from .forms import BrandForm, ColorForm, CarForm

def index(request):
    brands = Brand.objects.all()
    colors = Color.objects.all()
    cars = Car.objects.all()

    # Обработка формы для добавления бренда
    if request.method == 'POST' and 'add_brand' in request.POST:
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            Brand.objects.create(name=brand_form.cleaned_data['name'])
            return redirect('index')
    else:
        brand_form = BrandForm()

    # Обработка формы для добавления цвета
    if request.method == 'POST' and 'add_color' in request.POST:
        color_form = ColorForm(request.POST)
        if color_form.is_valid():
            Color.objects.create(name=color_form.cleaned_data['name'])
            return redirect('index')
    else:
        color_form = ColorForm()

    # Обработка формы для добавления автомобиля
    if request.method == 'POST' and 'add_car' in request.POST:
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            Car.objects.create(
                name=car_form.cleaned_data['name'],
                price=car_form.cleaned_data['price'],
                date_manufacture=car_form.cleaned_data['date_manufacture'],
                count=car_form.cleaned_data['count'],
                brand=car_form.cleaned_data['brand'],
                color=car_form.cleaned_data['color']
            )
            return redirect('index')
    else:
        car_form = CarForm()

    context = {
        'brands': brands,
        'colors': colors,
        'cars': cars,
        'brand_form': brand_form,
        'color_form': color_form,
        'car_form': car_form,
    }
    return render(request, 'index.html', context)
def edit_brand(request, brand_id):
    brand = Brand.objects.filter(id=brand_id).first()
    if not brand:
        return redirect('index')
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand.name = form.cleaned_data['name']
            brand.save()
            return redirect('index')
    else:
        form = BrandForm(initial={'name': brand.name})
    return render(request, 'edit_brand.html', {'form': form})

def edit_color(request, color_id):
    color = Color.objects.filter(id=color_id).first()
    if not color:
        return redirect('index')
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            color.name = form.cleaned_data['name']
            color.save()
            return redirect('index')
    else:
        form = ColorForm(initial={'name': color.name})
    return render(request, 'edit_color.html', {'form': form})

def edit_car(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if not car:
        return redirect('index')
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car.name = form.cleaned_data['name']
            car.price = form.cleaned_data['price']
            car.date_manufacture = form.cleaned_data['date_manufacture']
            car.count = form.cleaned_data['count']
            car.brand = form.cleaned_data['brand']
            car.color = form.cleaned_data['color']
            car.save()
            return redirect('index')
    else:
        form = CarForm(initial={
            'name': car.name,
            'price': car.price,
            'date_manufacture': car.date_manufacture,
            'count': car.count,
            'brand': car.brand,
            'color': car.color,
        })
    return render(request, 'edit_car.html', {'form': form})

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = CarForm()
    return render(request, 'create_car.html', {'form': form})
