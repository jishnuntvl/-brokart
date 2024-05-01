from django import template

register=template.Library()
@register.filter(name='chunks')
def chunks(lst,chunk_size):
    chunk=[]
    i=0
    for data in lst:
        chunk.append(data)
        i=i+1
        if i==chunk_size:
            yield chunk
            chunk=[]
            i=0
    if chunk:
        yield chunk