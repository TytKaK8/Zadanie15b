import streamlit as st
import reveal_slides as rs

# Заголовок страницы
st.set_page_config(page_title="Презентация: Шаблонный метод (Template Method)")

# Markdown для слайдов паттерна Template Method
template_markdown = r"""
# Паттерн: Шаблонный метод (Tem plate Method)

---

## Определение
**Template Method** — поведенческий паттерн, задающий скелет алгоритма, позволяя подклассам реализовать шаги.

---

## Мотивация
- Различные реализации алгоритма имеют схожую последовательность шагов.
- Необходимо избежать дублирования кода и обеспечить расширяемость.
- Пример: процесс обработки и сохранения данных.

---

## Структура
```text
AbstractClass
 ├─ template_method()
 │    ├─ step1()
 │    ├─ step2()   ← абстрактный
 │    └─ hook()    ← необязательный
 └─ ConcreteClass (реализует step2 и/или hook)
```

---

## Компоненты
- **AbstractClass** — определяет общий алгоритм и объявляет необходимые шаги.
- **ConcreteClass** — реализует абстрактные шаги.
- **Hook** — необязательные методы для расширения поведения.

---

## Пример кода на Python
```python
class AbstractClass:
    def template_method(self):
        self.step1()
        self.step2()
        self.hook()

    def step1(self):
        print("Шаг 1: базовая реализация")

    def step2(self):
        raise NotImplementedError("Должен быть реализован подклассом")

    def hook(self):
        pass

class ConcreteClassA(AbstractClass):
    def step2(self):
        print("Шаг 2: реализация для ConcreteClassA")

class ConcreteClassB(AbstractClass):
    def step2(self):
        print("Шаг 2: реализация для ConcreteClassB")

    def hook(self):
        print("Дополнительный шаг: hook в ConcreteClassB")

if __name__ == "__main__":
    for cls in (ConcreteClassA, ConcreteClassB):
        obj = cls()
        obj.template_method()
```

---

## Процесс выполнения
1. Клиент вызывает `template_method()`.
2. Базовые шаги (`step1`) выполняются по умолчанию.
3. Подклассы реализуют `step2`.
4. Опциональный `hook` добавляет дополнительное поведение.

---

## Когда использовать
- Алгоритм имеет фиксированную структуру, но детали могут меняться.
- Нужно избежать дублирования кода при разных реализациях.
- Важно централизованно контролировать порядок выполнения.

---

## Преимущества
- **Централизация алгоритма**: логика в одном месте.
- **Гибкость**: подклассы расширяют шаги.
- **Повторное использование**: базовая функциональность не дублируется.

---

## Недостатки
- **Рост иерархии**: больше классов.
- **Жесткая структура**: сложнее добавить новые шаги.
- **Снижение читаемости**: логика разбросана по классам.

---

## Сравнение с другими паттернами
- **Strategy**: меняет весь алгоритм на лету; Template Method фиксирует структуру.
- **Hook** похож на Observer, но обеспечивает скелет алгоритма.

---

## Реальные примеры
- Фреймворки тестирования (unittest, JUnit): последовательность `setUp`, `run_test`, `tearDown`.
- Java IO: `BufferedReader` управляет потоком, оставляя чтение данных подклассам.

---

## Лучшие практики
- Ограничить число абстрактных шагов.
- Предоставлять default-реализации для hook’ов.
- Документировать порядок шагов и варианты расширения.

---

## Итог
Паттерн Template Method формализует алгоритм, отделяя неизменяемые шаги от вариативных, что повышает поддерживаемость и расширяемость системы.

"""

# Основные элементы интерфейса
st.markdown("## Компонент STREAMLIT REVEAL.JS")
with st.sidebar:
    st.header("Параметры компонента")
    # Выбор темы
    theme = st.selectbox(
        "Тема",
        ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"],
        index=0
    )
    # Высота контейнера слайдов
    height = st.number_input("Высота контейнера", min_value=200, value=500)

    st.subheader("Настройки слайдов")
    content_height = st.number_input("Высота контента", min_value=200, value=900)
    content_width = st.number_input("Ширина контента", min_value=300, value=1000)
    scale_range = st.slider("Диапазон масштаба", min_value=0.1, max_value=5.0, value=(0.5, 3.0), step=0.1)
    margin = st.slider("Отступ", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
    plugins = st.multiselect(
        "Плагины",
        ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"],
        default=["highlight"]
    )

    st.subheader("Начальное состояние")
    hslidePos = st.number_input("Горизонтальная позиция", value=0)
    vslidePos = st.number_input("Вертикальная позиция", value=0)
    fragPos = st.number_input("Позиция фрагмента", value=-1)
    overview = st.checkbox("Показать обзор", value=False)
    paused = st.checkbox("Пауза", value=False)

currState = rs.slides(
    template_markdown,
    height=height,
    theme=theme,
    config={
        "width": content_width,
        "height": content_height,
        "minScale": scale_range[0],
        "maxScale": scale_range[1],
        "margin": margin,
        "center": True,
        "plugins": plugins
    },
    initial_state={
        "indexh": hslidePos,
        "indexv": vslidePos,
        "indexf": fragPos,
        "paused": paused,
        "overview": overview
    },
    markdown_props={"data-separator-vertical": "^--$"},
    key="template_method_presentation"
)

