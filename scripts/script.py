import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# Чтение входного файла
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)

# Подсчёт статистики
line_count = len(lines)
word_count = len(text.split())
char_count = len(text)

# Преобразование текста
processed_text = text.upper()

# Запись результата
with open(output_file, "w", encoding="utf-8") as f:
    f.write("=== Статистика текста ===\n")
    f.write(f"Строк: {line_count}\n")
    f.write(f"Слов: {word_count}\n")
    f.write(f"Символов: {char_count}\n\n")

    f.write("=== Обработанный текст в верхний регист ===\n")
    f.write(processed_text)
