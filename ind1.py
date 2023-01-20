# Задание 1
# Составить программу с использованием классов и объектов для решения задачи. Во всех
# заданиях, помимо указанных в задании операций, обязательно должны быть реализованы
# следующие методы:
# метод инициализации __init__ ; ввод с клавиатуры read ;вывод на экран display .
# Номер варианта определяется по формуле , где - номер
# студента по списку преподавателя. В раздел программы, начинающийся после инструкции if
# __name__ = '__main__': добавить код, демонстрирующий возможности разработанного класса.
# 1. Создать класс Vector3D, задаваемый тройкой координат. Обязательно должны быть
# реализованы: сложение и вычитание векторов, скалярное произведение векторов,
# умножение на скаляр, сравнение векторов, вычисление длины вектора, сравнение длины
# векторов.

class Vector3D(object):
	"""docstring for Vector3D"""
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	"""Сложение векторов"""
	def summation(self, x1, y1, z1):
		return self.x + x1, self.y + y1, self.z + z1

	"""Вычитание векторов"""
	def subtraction(self, x1, y1, z1):
		return self.x + (x1*(-1)), self.y + (y1*(-1)), self.z + (z1*(-1))

	"""Скалярное произведение"""
	def scalar_product(self, x1, y1, z1):
		return self.x * x1, self.y * y1, self.z * z1

	"""Умножение на скаляр"""
	def multiplication(self, n):
		return self.x * n, self.y * n, self.z * n

	"""Сравнение векторов"""
	def comparison(self, x1, y1, z1):
		if self.x == x1 and self.y == y1 and self.z == z1:
			return True
		else:
			return False

	"""Вычиление длинны вектора"""
	def vectlen(self):
		return (self.x**2 + self.y**2 + self.z**2)**(1/2)

	"""Сравнение длинн векторов"""
	def comparison_vect(self, x1, y1, z1):
		if (x1**2 + y1**2 + z1**2)**(1/2) == Vector3D.vectlen(self):
			return True
		else:
			return False

vect = Vector3D(3, 3, 3)
print(vect.summation(6, 6, 6))
print(vect.subtraction(6, 6, 6))
print(vect.multiplication(3))
print(vect.comparison(3,3,3))
print(vect.vectlen())
print(vect.comparison_vect(3,3,3))