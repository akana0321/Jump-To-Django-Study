import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 아래와 같은 어노테이션을 쓰면 템플릿에서 해당 함수를 필터로 사용 가능
@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"] # n12br은 줄바꿈 문자를 <br>로 바꿔줌, fenced_code는 마크다운의 소스코드 표현을 위해 필요
    return mark_safe(markdown.markdown(value, extensions=extensions))