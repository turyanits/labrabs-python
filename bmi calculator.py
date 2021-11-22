"""
Tracking your BMI is a useful way of cheking of you're maintaining a healthy weight.
Weight is in kilograms, height is in meters.
Sample input:
85
1.9
"""

Weight = int(input('Weight:'))
Height = float(input('Height:'))
bmi = Weight / Height ** 2
print(bmi)

if bmi <= 18.5:
    print('Underweight.')
if 18.5 <= bmi <= 25:
    print('Normal.')
if 25 <= bmi <= 30:
    print('Overweight.')
if bmi >= 30:
    print('Obesity.')
