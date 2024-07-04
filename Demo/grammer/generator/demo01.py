def gen_range(stop):
    i=0
    while i<stop:
         yield i
         i=i+1

it=gen_range(5)
while True:
    try:
        print(next(it),end=",")
    except StopIteration:
        break