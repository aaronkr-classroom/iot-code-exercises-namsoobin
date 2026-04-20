class RoomSensor:
    from RoomSensor import Kitchen, Bedroom, Balcony
    
    def show_info(self, name, temperature, humidity, light):
        #속성 초기화
        self.name=input()
        self.temperature = int(input())
        self.humidity = int(input())
        self.light = int(input())
        
        print(f'Sensor : {name}')
        print(f'Temperature : {temperature}')
        print(f'Humidity :{humidity}')
        print(f'Light : {light}')
        
    def confort_level():
        if (20<=temperature<=26) and (40<=humidity<=60):
            print("Comfortable")
        elif (temperature >= 30) and (humidity >= 70):
            print("Warining")
        else :
            print("Normal")
    def light_status():
        if light < 200 :
            print("Dark")
        if light > 200 :
            print("Bright")
    Kitchen = name
    Bedroom = light
    Balcony = humidity
    List1 = [Kitchen, Bedroom, Balcony]
    
    for i in range(3):
        show_info()
        confort_level()
        light_status()