"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from itertools import product


stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
        ]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_all = 0
    stock_avg = 0
    stock_counter = 0

    for phone in stock:
        sales_total = sum(phone['items_sold'])
        print(f'Суммарное количество продаж для {phone["product"]} - {sales_total}')
        sales_avg = sales_total / len(phone['items_sold'])
        print(f'Среднее количество продаж  {phone["product"]} - {round(sales_avg, 2)}')
        sum_all += sales_total
        stock_counter += len(phone['items_sold'])

    print(f'Суммарное количество продаж всех товаров - {sum_all}')
    stock_avg = sum_all / stock_counter
    print(f'Среднее количество продаж {round(stock_avg, 2)}')
  


    
if __name__ == "__main__":
  main()