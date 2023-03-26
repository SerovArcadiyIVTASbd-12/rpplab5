import machine
import csv


def write(weather_obj):
    csvfile = open('table.csv', 'a', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(weather_obj)
    csvfile.close()


def out():
    list_reader = machine.read_from()
    machine.sorter(list_reader)


if __name__ == '__main__':
    do = int(input("Вывод csv - 1\tДобавить в csv - 2\n"))
    if do == 1:
        out()
    else:
        weather_obj = machine.WeatherData()
        freq, powering, temp, number = map(float, input("Введите параметры: частота вибрации, "
                                                                    "потребление, температура, "
                                                                    "номер станка: ").split())
        weather_obj.freq = freq
        weather_obj.powering = powering
        weather_obj.temp = temp
        weather_obj.number = number


        print(weather_obj)
        write(weather_obj)


