from openpyxl import load_workbook, Workbook
import statistics

# Выполнили: Шишков Л.А., Язданов Р.Н.

class StatisticsL():        
    def statisticV(name):                           #метод расчёта числовых характеристик выборки
        dlina = len(name)                           #размер выборки
        srednee = statistics.mean(name)             #среднее значение выборки
        dispersia = statistics.variance(name)       #дисперсия выборки
        sko = statistics.stdev(name)                #СКО выборки
        try:                                        #мода выборки
            moda = statistics.mode(name)
        except:
            moda = "-"
        mediana = statistics.median(name)           #медиана выборки
    def sortedV(name):                              #метод сортировки выборки
        sort = sorted(name)                         #отсортированная выборка

