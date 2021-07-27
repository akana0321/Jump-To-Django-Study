from django import template

register = template.Library()

# 아래와 같은 어노테이션을 쓰면 템플릿에서 해당 함수를 필터로 사용 가능
@register.filter
def sub(value, arg):
    return value - arg