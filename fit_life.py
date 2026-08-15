print('Привет!','Я виртуальный помощник от Fitlife!')
print('Мне потребуются твои данные для расчета ИМТ.')
name = input('Как я могу к тебе обращаться?')
print(f'{name.title()},рад знакомству!')
user_age = int(input('Введи свой возраст : ')) 
user_weight = float(input('Введи свой вес в кг : '))
user_height = float(input('Введи свой рост в м (пример - 1.55): '))

'''Расчет ИМТ'''
bmi = user_weight / (user_height ** 2)
print(f'Твой индекс массы тела (ИМТ) : {round(bmi,1)}')

def water_intake_recommendations(bmi):
    if bmi < 18.5: 
        return user_weight * 0.030
    elif 18.5 <= bmi < 25:
        return user_weight * 0.030
    else:
        return user_weight * 0.030
water_intake = water_intake_recommendations(bmi)

print(f'Твой индекс массы тела (ИМТ): {bmi:.2f}')
print(f'Твоя норма суточного потребления воды:{water_intake:.2f} литров.')
