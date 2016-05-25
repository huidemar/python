import datetime

semana = ['Segunda-Feira', 'Terca-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo']
data = datetime.datetime.today()
print semana[data.weekday()]
