from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from datetime import datetime
from .models import Choice, Question, Good, Cart
from django.db.models import Q # new
from django.contrib.auth.decorators import login_required

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def catalog(request):
    # if type.equals('all'):
    objects = Good.objects.all()
    print(objects)
    # else:
    #     objects = Question.objects.filter(Q(question_text__icontains=type))

    context = {'goods_list': objects}
    return render(request, 'polls/catalog.html', context)


def detail(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    return render(request, 'polls/detail.html', {'good': good})

@login_required
def cartView(request, user_id=1):
    try:
        # goodsAtCart = Good.objects.all()
        print("WASS",request.user)
        goodsInCart = Cart.objects.filter(user=request.user)
        goods_id = []
        for g in goodsInCart:
            goods_id.append(g.good_id)
        print(goods_id)
        # goodsAtCart = Good.objects.all()
        goodsAtCart = []
        for gid in goods_id:
            goodsAtCart.append(Good.objects.get(pk=gid))
        print(goodsAtCart)

        user = 1
        # goodsAtCart = Cart.objects.filter(Q(user_id__icontains=user))
    except EnvironmentError:
        # Redisplay the question voting form.
        return render(request, 'polls/cartView.html', {
            'cart': 1,
            'error_message': "You didn't select a choice.",
        })
    else:
        return render(request, 'polls/cartView.html', {'goodsAtCart': goodsAtCart})

@login_required
def userCabinet(request, user_id=1):
    try:
        # goodsAtCart = Good.objects.all()
        print("WASS",request.user)
        goodsInCart = Cart.objects.filter(user=request.user)
        goods_id = []
        for g in goodsInCart:
            goods_id.append(g.good_id)
        print(goods_id)
        # goodsAtCart = Good.objects.all()
        goodsAtCart = []
        for gid in goods_id:
            goodsAtCart.append(Good.objects.get(pk=gid))
        print(goodsAtCart)

        user = 1
        # goodsAtCart = Cart.objects.filter(Q(user_id__icontains=user))
    except EnvironmentError:
        # Redisplay the question voting form.
        return render(request, 'polls/userCabinet.html', {
            'cart': 1,
            'error_message': "You didn't select a choice.",
        })
    else:
        return render(request, 'polls/userCabinet.html', {'goodsAtCart': goodsInCart, 'user': request.user})


def addToCart(request, good_id):
    good = Good.objects.get(id=good_id)
    cart = Cart(user=request.user, good=good, order_date=datetime.now())
    cart.save()
    response = "Good added"
    return HttpResponseRedirect(reverse('polls:detail', args=(good_id,)))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def search(request):
    # question = get_object_or_404(Question, pk=question_id)
    try:
        # print(Question.objects.get(question_text=request.GET['searched_text']))
        query = request.GET.get('searched_text')
        selectedQuestions = Good.objects.filter(Q(good_name__icontains=query) | Q(good_description__icontains=query))
        for obj in selectedQuestions:
            print(obj)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': selectedQuestions,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'polls/searchResults.html', {'results': selectedQuestions})