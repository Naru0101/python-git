'''
5.1 f(x) = 1: Возвращает всегда одно и то же значение, независимо от входных данных. Это означает, что функция является последовательной, так как для одного и того же входа всегда будет возвращаться одно и то же значение. Следовательно, функция является последовательной.

5.2 f(x) = rand(): Возвращает случайное число, которое может изменяться при каждом вызове функции. Поскольку результат функции меняется при каждом вызове, она не является последовательной.

5.3 f(x) = next_empty_slot(): Возвращает индекс следующего пустого элемента в хеш-таблице. Если хеш-таблица не изменяется, то функция будет возвращать одно и то же значение для одного и того же состояния хеш-таблицы. Таким образом, эта функция является последовательной.

5.4 f(x) = len(x): Возвращает длину строки, которая является входным значением. Поскольку длина строки зависит от содержания строки, результат функции будет разным для разных строк. Поэтому эта функция не является последовательной.

5.5 Телефонная книга: В этом случае хеш-функция должна обеспечить равномерное распределение имен по хеш-таблице. Поскольку имена имеют различные начальные буквы, хеш-функция, которая использует первый символ строки в качестве индекса, может привести к плохому распределению, так как все имена начинаются с разных букв. Лучше всего подходит хеш-функция, которая использует длину строки в качестве индекса, так как длины имен могут сильно различаться, что способствует более равномерному распределению.

5.6 Размеры батареек: В этом случае хеш-функция, которая ставит в соответствие каждой букве простое число и затем использует остаток от деления суммы всех значений на размер хеша, обеспечит хорошее распределение, так как размеры батареек имеют разные символы и различаются по размеру, что способствует равномерному распределению.

5.7 Связь названий книг с именами авторов: В этом случае названия книг имеют разные первые буквы, поэтому хеш-функция, которая использует первый символ строки в качестве индекса, может привести к плохому распределению. Также использование длины строки в качестве индекса может быть неэффективным, так как названия книг могут быть разной длины. Хеш-функция, которая ставит в соответствие каждой букве простое число и использует остаток от деления суммы всех значений на размер хеша, может обеспечить более равномерное распределение.
'''