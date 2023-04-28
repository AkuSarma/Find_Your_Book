from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Order
from django.urls import reverse_lazy
from django.db.models import Q  # for search method
from django.http import JsonResponse
import json


class BooksListView(ListView):
    model = Book
    template_name = 'list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'


class SearchResultsListView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url = 'login'


class BookSellView(CreateView):
    model = Book
    template_name = 'sell_book.html'
    fields = ["title", "author", "description", "price", "image_url", "follow_author", "book_available"]
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.upload_by = self.request.user
        return super(BookSellView, self).form_valid(form)


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    product = Book.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )
    return JsonResponse('Payment completed!', safe=False)

def bid_price(request, seller):
    data = {
        'seller_name':seller,
    }
    return render(request, "bid_price.html", data)