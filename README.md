# Snakemake

## 1. Клонирование репозитория

```bash
git clone https://github.com/<USERNAME>/snakemake.git
```

### Перейти в каталог проекта:

```bash
cd snakemake
```

## 2. Проверка Python

```bash
py --version
```

Ожидаемый вывод, например:

```bash
Python 3.11.9
```

## 3. Установка Snakemake

```bash
py -m pip install --upgrade pip
py -m pip install snakemake
```

## 4. Проверка установки Snakemake

```bash
py -m snakemake --version
```

Ожидаемый вывод, например:

```bash
9.14.5
```

## 5. Dry-run (проверка workflow без выполнения)

```bash
py -m snakemake -n
```

Ожидаемый вывод:

```bash
rule process_text:
    input: data/input.txt
    output: results/output.txt
```

## 6. Запуск workflow

```bash
py -m snakemake --cores 1
```

## 7. Проверка результата

```bash
type results\output.txt
```

Ожидаемый вывод:

```bash
Hello from input file!
Processed by Snakemake workflow.
```