#a = int(input("donne moi a = "))
#b = int(input("donne moi b = "))
#c = int(input("donne moi une nombre = "))
#d = int(input("donne moi la limite = "))


def plus_grand_reels(a: int, b : int) -> int:
    if a > b:
        return a
    else :
        return b

def limit(c:int,d:int) -> str:
    if c > d:
        return "you have passed the limit"
    else:
        return "good boy"

def grand_liste(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

def mini(*args) -> int:
  b = 3
  total = 0
  for i in args:
      if i < b:
          total += 1
    return total

def ensemble()
#print(f"the plus grand is : {plus_grand_reels(a, b)}")
#print(limit(c,d))
print(liste(10,5,4,11))