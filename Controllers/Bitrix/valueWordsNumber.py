from num2words import num2words

def valueWordsNumber(monthlyAmount):

      # Valor Mensal por Extenso
      extenso = num2words(monthlyAmount, lang='pt_BR')
      wordsMonthValue=f"R$ {monthlyAmount} ({str(extenso).upper()} REAIS)"

      return wordsMonthValue

