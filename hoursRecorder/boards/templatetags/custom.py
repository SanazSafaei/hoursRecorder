from django import template
from datetime import datetime

register=template.Library()

@register.filter(name='dec')
def dec(value1=None ,value2=None):
    if (value1!=None):
        end=str(value1).split()
        start=str(value2).split()
        delta =[]
    
        end=end[1].split(':')
        start=start[1].split(':')
    
        delta.append(str(int(end[0])-int(start[0])))
        delta.append(str(int(end[1]) - int(start[1])))
    
        return (delta[0]+" ساعت و "+delta[1]+" دقیقه ")
    else:
        
        return ("...")
