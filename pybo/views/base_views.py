from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    pageno=request.GET.get('page','1')
    question_list=Question.objects.order_by('-create_date')
    pages=Paginator(question_list,10)
    onepage=pages.get_page(pageno)
    context={'ql':onepage}
    #return HttpResponse("안녕하세요. pybo에 오신것을 환영합니다.")
    return render(request,'pybo/question_list.html',context)

def detail(request,question_id):
    #question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question,pk=question_id)
    # select * from question where id=question_id
    context={'question':question}
    return render(request,'pybo/question_detail.html',context)