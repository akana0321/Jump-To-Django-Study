# 기본관리
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question # 상위 폴더의 models에 접근하기 때문에 .. 찍어준 것

def index(request):
    ''' pybo 목록 출력 '''
    #입력 파라미터
    page = request.GET.get('page', 1) # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 한 페이지당 10개 씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # pybo 내용 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)
