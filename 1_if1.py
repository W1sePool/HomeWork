"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input("Введите возраст "))
def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
if age < 0 :
  print("Введите корректный возраст")
elif age >0 and age <3:
  print ("Совсем малыш , сиди дома")
elif age <7:
  print("Учись в детком саду!")
elif age <=17:
  print("Учись в школе ")
elif age <=24:
  print ("учись в вузе ")
elif age <=65:
  print("Пора на работу")
else:
  print("Введите корректный возраст")


    

# if __name__ == "__main__":
  #  main()
