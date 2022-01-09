# 	CLASS ---Representation of data member and behavior of object is known as CLASS.
# OBJECT--An instance of class is nothing but OBJECT.

# REFERANCE VARIABLE- The variable wihich is used to refer object.
 
#  EX-- 

# class test:
# 	def __init__(self):
# 		print('hello world')
# t=test()
# ----------------------------------------
#    MINI APPLICATION
# ----------------------------------------
# class movie:
# 	def __init__(self,title,hero,herohin):
# 		self.title=title
# 		self.hero=hero
# 		self.herohin=herohin

# 	def info(self):
# 		print('NAME OF THE TITLE IS:',self.title)
# 		print('NAME OF THE HERO IS:',self.hero)
# 		print('NAME OF THE HEROHIN IS:',self.herohin)

# list_of_movies=[]
# while True:
# 	title=input('NAME OF THE TITLE IS:')
# 	hero=input('NAME OF THE HERO IS:')
# 	herohin=input('NAME OF THE HEROHIN IS:')
# 	m=movie(title,hero,herohin)
# 	list_of_movies.append(m)
# 	print('MOVIE ADDED SUCCESSFULLY')
# 	option=input('DO YOU ADD ONE OR MORE MOVIES:')
# 	if option.lower()=='no':
# 		break
# 	print(' ALL MOVIE INFO---')
# for movie in list_of_movies:
# 	movie.info()
# 	print()



# INNER CLASS

# class outer:
# 	def __init__(self):
# 		print('outer class object')
# 	class inner:
# 		def __init__(self):
# 			print('inner class object')
# 		def m(self):
# 			print('inner class method')
	
# #o=outer()
# #i=o.inner()
# #i.m()
# outer().inner().m()

# EG-2

# class Human:
# 	def __init__(self,name):
# 		print('HUMAN OBJECT CREATION')
# 		self.name=name
# 		self.head=self.Head()
# 	def info(self):
# 		print('Hello ,My Name is:',self.name)
# 		self.head.talk()
# 		self.head.brain.think()

# 	class Head:
# 		print('HEAD OBJECT CREATION')
# 		def __init__(self):
# 			self.brain=self.Brain()
# 		def talk(self):
# 			print('Talking...')

# 		class Brain:
# 			def __init__(self):
# 				print('BRAIN OBJECT CREATION')
# 			def think(self):
# 				print('Thinking......')

# human=Human('BUBU')
# human.info()

# EG-3

# class Wood:
# 	def __init__(self):
# 		print('WOOD OBJECT CREATION')
# 		self.chair=self.Chair()
# 	def info(self):
# 		print('WOOD COOLECTED FROM FOREST')
# 		self.chair.make()
# 		self.chair.shop.sell()
# 		self.chair.shop.home.enjoy()
# 	class Chair:
# 		def __init__(self):
# 			print('CHAIR OBJECT CREATED')
# 			self.shop=self.Shop()
# 		def make(self):
# 			print('CHAIR MADE FROM WOOD')
# 		class Shop:
# 			def __init__(self):
# 				print('SHOP OBJECT CREATED')
# 				self.home=self.Home()
# 			def sell(self):
# 				print('CHAIR READY FOR SELL')
# 			class Home:
# 				def __init__(self):
# 					print('HOME OBJECT CREATED')
# 				def enjoy(self):
# 					print('FINNALY YOU SIT IN CHAIR')

# wood=Wood()
# wood.info()


# EG-3

# class Earth:
# 	def __init__(self):
# 		print('Earth oBject creation')
# 		self.sky=self.Sky()
# 	def info(self):
# 		print('EVERY ONE UNDER THE EARTH')
# 		self.sky.sky1()
# 		self.sky.cloud.cloud1()
# 		self.sky.cloud.land.land1()
# 		self.sky.cloud.land.human.human1()

# 	class Sky:
# 		def __init__(self):
# 			print('Sky object Created')
# 			self.cloud=self.Cloud()
# 		def sky1(self):
# 			print('SKY IS BLUE')

# 		class Cloud:
# 			def __init__(self):
# 				print('CLOUD OBJECT CREATED')
# 				self.land=self.Land()
# 			def cloud1(self):
# 				print('CLOUD IS UNDER THE SKY')

# 			class Land:
# 				def __init__(self):
# 					print('LAND OBJECT CREATED')
# 					self.human=self.Human()
# 				def land1(self):
# 					print('LAND IS A LIVING SURFACE')

# 				class Human:
# 					def __init__(self):
# 						print('HUMAN OBJECT CREATED')
# 					def human1(self):
# 						print('HUMAM IS GOD GIFTED')



# e=Earth()
# e.info()


# INHERITANCE 

# class P:
# 	def m(self):
# 		print('PARENT METHOD')
# class C(P):
# 	def n(self):
# 		print('CHILD METHOD')
# c=C()
# c.m()
# c.n()

# POLYMERPHYSIM
 
# class P:
# 	def marry(self):
# 		print('SUBHALAXMI')
# class C(P):
# 	pass
# c=C()
# c.marry()


# class P:
# 	def marry(self):
# 		print('SUBHALAXMI')
# class C(P):
# 	def m(self):
# 		print('APPALAMMA')
# c=C()
# c.m()
# c.marry()

