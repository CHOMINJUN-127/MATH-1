import math
from fractions import Fraction

# 주어진 값
a = 10
b = 8

# sin 60° = √3 / 2
sqrt3 = math.sqrt(3)
sin_60 = sqrt3 / 2

# sin B = (b * sin 60°) / a
sin_B = (b * sin_60) / a

# sin^2 B = (sin B)^2
sin_B_squared = sin_B ** 2

# cos^2 B = 1 - sin^2 B
cos_B_squared = 1 - sin_B_squared

# 분수로 변환 (12/25, 13/25)
sin_B_frac = Fraction(12, 25)
cos_B_frac = Fraction(13, 25)

print("sin^2 B =", sin_B_frac)
print("cos^2 B =", cos_B_frac)


from fractions import Fraction
import math
import turtle

# 거리 및 각도
a = 8      # B-사용자
c = 10     # A-사용자
angle_A_deg = 60
angle_A_rad = math.radians(angle_A_deg)

# 코사인 60도는 1/2
cos_A = Fraction(1, 2)

# AB^2 구하기
b2 = c**2 + a**2 - 2 * c * a * cos_A
# b = math.sqrt(float(b2))  # 필요하면 실수로 변환

# cos B 구하기
numerator = a**2 + c**2 - b2
denominator = 2 * a * c
cos_B = Fraction(numerator, denominator)
cos2_B = cos_B ** 2

print(f"cos^2 B = {cos2_B} (= {float(cos2_B):.2f})")

# turtle로 삼각형 그리기 (생략 가능)
scale = 30
A = (0, 0)
User = (c * scale, 0)
Bx = a * math.cos(math.pi - angle_A_rad)
By = a * math.sin(math.pi - angle_A_rad)
B = (Bx * scale, By * scale)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(A)
t.pendown()
t.dot(10, "red")
t.write("A (위성A)", align="right")
t.goto(User)
t.dot(10, "blue")
t.write("U (사용자)", align="left")
t.goto(B)
t.dot(10, "green")
t.write("B (위성B)", align="center")
t.goto(A)
turtle.done()
