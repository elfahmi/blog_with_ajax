from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View

from .models import Page, Comment
from .forms import CommentForm


def home(request):
    pages = Page.objects.all()   
    context = {'pages': pages}
    return render(request, 'home.html', context)


class Detail(View):
    def get(self, request, page_id):
        page = get_object_or_404(Page, id=page_id)
        form = CommentForm()
        context = {'page': page, 'form': form}
        return render(request, 'detail.html', context)

    def post(self, request, page_id):
        page = get_object_or_404(Page, id=page_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_com = form.save(commit=False)
            new_com.page = page
            new_com.save()
            return JsonResponse({'page': model_to_dict(new_com)}, status=200)
        else:
            return redirect('detail', page.id)


class Delete(View):
    def post(self, request, page_id):
        comment = get_object_or_404(Comment, id=page_id)
        comment.delete()
        return JsonResponse({'result': 'ok'}, status=200)