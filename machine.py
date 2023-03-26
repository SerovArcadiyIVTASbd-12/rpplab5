import time



class Position:
#№ показания, дата и время, частота вибрации, потребляемая мощность, температуры, номер станка
    def __init__(self, pos, freq, powering, temp, number):
        self.pos = int(pos)
        self.freq = float(freq)
        self.powering = float(powering)
        self.temp = float(temp)
        self.number = float(number)


class WeatherData(Position):

    def __init__(self, pos=-1, freq=0.0, powering=0.0, temp=0.0, number=0.0,
                 date=time.strftime("%Y-%m-%d %H:%M")):
        super().__init__(pos, freq, powering, temp, number)
        self.date = date
        if self.pos == -1:
            WeatherData.last_n(self)

    def __repr__(self):
        return f"WeatherData(id={self.pos}, fre={self.freq}, power={self.powering}, tem={self.temp}, " \
               f"num={self.number}, date={self.date})"

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getitem__(self, index):
        return [self.pos, self.freq, self.powering, self.temp, self.number, self.date][index]

    def __iter__(self):
        return iter([self.pos, self.freq, self.powering, self.temp, self.number, self.date])

    @classmethod
    def from_string(cls, string):
        _id, fre, power, tem, num, date = string.strip().split(",")
        return cls(int(_id), float(fre), float(power), float(tem), float(num), date)

    def generator(self):
        for i in self:
            yield i

    def last_n(self):
        ar = read_from()
        if ar:
            n = ar[-1].pos + 1
        else:
            n = 1
        self.pos = n


def read_from(path="table.csv"):
    csvfile = open(path, 'r+', newline='')
    _list = []
    if csvfile != 0:
        for i in csvfile.readlines():
            _list.append(WeatherData.from_string(i))
        return _list
    else:
        return 0


def sorter(list_reader):
    print("Сортировка по строке (дате):")
    for i in sorted(list_reader, key=lambda d: d.date, reverse=True):
        print(i)

    print("\nСортировка по частоте:")
    for i in sorted(list_reader, key=lambda d: float(d.freq)):
        print(i)

    print("\nВывод данных значения температуры, которая превышает 5 градусов по цельсию:")
    for i in list_reader:
        if float(i.temp) > 35:
            print(i)

if __name__ == '__main__':
    weather = WeatherData()

    weather.freq = 11  # Проверка __setatr__
    weather.powering = 7.2
    weather.temp = 4
    weather.number = 12

    print(weather, "Проверка __repr__\n")  # Проверка __repr__

    print(weather[2], "Проверка __getitem__\n")  # Проверка __getitem__

    for i in weather:  # Проверка __iter__
        print(i, end=' ')
    print("Проверка __iter__\n")

    print(weather.generator(), "Проверка generator")  # Проверка generator
    print(*weather.generator(), "\n")

    print(read_from())  # Проверка static метода


