from datetime import date
from dateutil.relativedelta import relativedelta

def calculator(n1,n2, typeOf):
   match typeOf:
    case "Adição":
         return str(n1 + n2)
    case "Subtração":
         return str(n1 - n2)
    case "Multiplicação":
         return str(n1 * n2)
    case "Divisão":
        return str(n1 / n2)
    
    
def idade(birthdate):
    return str(date.today().year - birthdate.year)

def difDatas(d1, d2):
    di = abs(relativedelta(d1, d2))
    return (f'{di.years} anos, {di.months} meses, {di.days} dias.')

def color_notes(val):
    color = ''
    if val in [3, 4]: color = 'color: green'
    elif val in [1, 2]: color = 'color: red'
    return color