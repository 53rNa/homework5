# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = tuple ([5, 9, True, "Def"])         # Создаем кортеж из нескольких элементов разных типов данных
print (immutable_var)                               # с выводом на экран

mutable_list = [5, "string", 45]                    # Создаем список из нескольких элементов разных типов данных
print (mutable_list)                                # с выводом на экран

mutable_list[0] = 80                                # Изменяем элементы списка
mutable_list[-1] = 100
print (mutable_list)                                # Выводим на экран измененный список