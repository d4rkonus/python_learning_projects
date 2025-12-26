#!/usr/bin/python3

class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(t): #(t) == temperature
        return (t * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(t): #(t) == temperature
        return (t - 32) * 5/9


temp_c = 25
temp_f = 50

print(f"\n[+] {temp_c}°C son {TemperatureConverter.celsius_to_fahrenheit(temp_c)}°F")
print(f"\n[+] {temp_f}°F son {TemperatureConverter.fahrenheit_to_celsius(temp_f):.2f}°C\n")