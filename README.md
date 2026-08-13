# FitLife
print('Привет! Я виртуальный помощник от Fitlife!')
print('Я подготовлю для тебя индивидуальные рекомендации.')
print('Мне потребуются твои данные.')

name = input('Как я могу к тебе обращаться?')
print(f'{name.capitalize()},рад знакомству!')
user_age = int(input('Введи свой возраст : '))
user_weight = float(input('Введи свой вес в кг : '))
user_height = float(input('Введи свой рост в метрах(например, 1.55) : '))
bmi = user_weight / (user_height ** 2)
print(f'Твой индекс массы тела (ИМТ) : {round(bmi,1)}')

def water_intake_recommendations(bmi):
    if bmi < 18.5: 
        return user_weight * 0.030
    elif 18.5 <= bmi <25:
        return user_weight * 0.030
    else:
        return user_weight * 0.030
water_intake = water_intake_recommendations(bmi)
print(f'Твоя норма суточного потребления воды : {water_intake} литров.','Следуй рекомендациям и будь здоров!',sep=' ')
