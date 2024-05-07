from django.shortcuts import render,redirect
from .models import Item,Consume
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['food']
        food_data = Item.objects.get(name=name)
        user = request.user
        consume = Consume(user=user,item_name=food_data)
        consume.save()
        return redirect('home')
    food = Item.objects.all()
    consumed_food = Consume.objects.filter(user = request.user)
    return render(request,'index.html',{'food':food,'consume':consumed_food})

def delete(request,id):
    data = Consume.objects.get(id=id)
    data.delete()
    return redirect('home')