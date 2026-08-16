
print('Привет!', 'Я виртуальный помощник от Fitlife!')
print('Мне потребуются твои данные для расчета ИМТ.')
name = input('Как я могу к тебе обращаться?')
formatted_name = name.title()
print(f'{formatted_name}, рад знакомству!')
age = int(input('Введи свой возраст : '))
weight = float(input('Введи свой вес в кг : '))
height = float(input('Введи свой рост в м (пример - 1.55): '))

"""Расчет ИМТ"""
bmi = weight / (height ** 2)


def water_intake_recommendations(bmi: float, weight: float) -> float:
    """Recommend daily water intake in liters based on BMI and weight."""
    if bmi < 18.5:
        return weight * 0.028
    elif 18.5 <= bmi < 25:
        return weight * 0.030
    else:
        return weight * 0.035


water_intake = water_intake_recommendations(bmi, weight)


print(f'Твой индекс массы тела (ИМТ): {bmi:.2f}')
print(f'Твоя норма воды в сутки:{water_intake:.2f} литров.')
