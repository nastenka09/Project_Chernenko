'''
#Задание.Книжные магазины предлагают следующие коллекции книг.
Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
БукМаркет – Пушкин, Достоевский, Маяковский.
Галерея – Чехов, Тютчев, Пушкин. Определить:
1. Полный список всех книг магазинов.
2. Какие книги есть во всех магазинах.
3. Хотя бы одну книгу, которая есть не во всех магазинах.
'''

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

all_books = magistr | domknigi | bukmarket | galereya

common_books = magistr & domknigi & bukmarket & galereya

example_book = None
for book in all_books:
    if not (book in magistr and book in domknigi and
            book in bukmarket and book in galereya):
        example_book = book
        break

print("1. Полный список всех книг магазинов:", sorted(all_books))
print("2. Книги, которые есть во всех магазинах:", common_books)
if example_book:
    print(f"3. Пример книги, которая есть не во всех магазинах: '{example_book}'")
else:
    print("3. Все книги есть во всех магазинах")







