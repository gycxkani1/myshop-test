from django import template
register = template.Library() # 创建一个注册对象
#注册为过滤器
@register.filter
def show_title(value,n):
  if len(value) > n:
    return f'{value[0:n]}...'
  else:
    return value