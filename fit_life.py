# Fit_Life project

WATER_COAFF_UNDERWEIGHT = 0.028
WATER_COAFF_NORMAL = 0.030
WATER_COAFF_OVERWEIGHT = 0.035


def recommendations(bmi, weight):
    '''Return the multiplication of two multupliers(bmi and weight)'''
    if bmi < 18.5:
        return weight * 0.028
    elif 18.5 <= bmi < 25:
        return weight * 0.030
    else:
        return weight * 0.035


print('Привет! Я виртуальный помощник от Fitlife!')
print('Мне потребуются твои данные для расчета ИМТ.')
name = input('Как я могу к тебе обращаться?')
print(f'{name.title()}, рад знакомству!')
user_age = int(input('Введи свой возраст:'))

weight = float(input('Введи свой вес в кг:'))
height = float(input('Введи свой рост в метрах (пример: 1.55):'))
bmi = weight / (height ** 2)
print(f'Твой индекс массы тела (ИМТ): {round(bmi, 1)}')
water_intake = recommendations(bmi, weight)
water_intake = (
    f'Твоя норма суточного потребления воды:\n'
    f'  {water_intake} литров.\n'
)
# print(f'')
print('Следуй рекомендациям и будь здоров!')
