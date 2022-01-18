import math as m

def get_area(radius):
    area=m.pi*m.pow(radius, 2)
    return area

radius=int(input('諛섏��由꾩쓣 �엯�젰�빐二쇱꽭�슂 : '))
area=get_area(radius)

print('�꼻�씠 : ',area)