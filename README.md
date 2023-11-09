# doctor_free_time_windows

[![Test Suite](https://github.com/alexpro2022/doctor_free_time_windows/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/doctor_free_time_windows/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/alexpro2022/doctor_free_time_windows/graph/badge.svg?token=rcYWiP1mSE)](https://codecov.io/gh/alexpro2022/doctor_free_time_windows)

<details>
<summary>Тестовое задание</summary>
Доктор принимает с 9 утра до 9 вечера.
Часть времени у него занята: приемы, обед, уборка кабинета.

```py
busy = [
    {'start' : '10:30',
    'stop' : '10:50'
    },
    {'start' : '18:40',
    'stop' : '18:50'
    },
    {'start' : '14:40',
    'stop' : '15:50'
    },
    {'start' : '16:40',
    'stop' : '17:20'
    },
    {'start' : '20:05',
    'stop' : '20:20'
    }
]
```

Требуется сформировать список свободных окон по 30 минут.

</details>

<br>

## Оглавление
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![pre-commit](https://img.shields.io/badge/-pre--commit-464646?logo=pre-commit)](https://pre-commit.com/)

<br>

## Установка и запуск:
1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
git clone https://github.com/alexpro2022/doctor_free_time_windows.git
cd doctor_free_time_windows
```

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Для запуска приложения выполните команду:
```bash
python main.py
```

5. Для запуска тестов выполните команду:
```bash
pytest
```

[⬆️Оглавление](#оглавление)

<br>

## Удаление:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr doctor_free_time_windows && deactivate
```

[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#doctor_free_time_windows)
