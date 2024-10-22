Жадібний алгоритм виявився найшвидшим при великій сумі, його часова складність приблизно $O(n)$. Алгоритм динамічного програмування більш повідльний при великій сумі та має часому складність $O(n \cdot M)$, де М це сума, оскільки для визначення оптимального числа монет, алгоритм проходить по кожному номіналу для кожної суми. Для цієї задачі жадібний алгоритм не завжди може дати правильний розв'язок. Наприклад, суму 10 копійок монетами вартістю 1, 5 і 6 коп. жадібний алгоритм розміняє так: 6 коп. — 1 шт., 1 коп. — 4 шт., в той час як правильний розв'язок — 2 монети по 5 копійок.

Отже, алгоритм динамічного програмування більш точний, але вимагає більше обчислювального часу для великих сум, а жадібний алгоритм навпаки досить швидкий, проте має недолік в неточності обрахунків за певних умов.