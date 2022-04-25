per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Сколько "резаных бумажек" Вы планируете разместить на депозит?'))
deposit = list(per_cent.values())
for num in range(len(deposit)): deposit[num] = round(deposit[num] * money / 100 , 2)
print('Вот сколько получите за год:' , deposit)
print('Максимальная сумма, которую вы можете заработать- ' , max(deposit))