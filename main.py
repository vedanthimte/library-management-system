#Library Management system
#MADE BY VEDANT HIMTE (KING YASHRAJ)

import time 
from datetime import datetime

now = datetime.now()
current = now.strftime(f"[ %Y-%m-%d %H:%M:%S ]")
 
class Library:
	def __init__(self, books_list,  name):
		self.library_name = name
		self.books_list = books_list
		self.nav_books = []
		self.av_books = books_list
		
	def display_books(self):
		books = self.books_list
		print("\n List Of all BOOKS: ")
		for b in books :
			i = "~"
			print(f"{i} {b}")
		print("\n ",25*"-")
						
	def add_books(self):
		a = input("\n Name of Book: ")
		self.books_list.append(a)
		with open("books_list.txt", "a") as f:
			f.write(f"{a}\n")
		with open("av.txt", "a") as ff:
			ff.write(f"{a}\n")
		print("Added successfuly... \n ")
		print("\n ",25*"-")
		
	def lend_books(self):
		print("Choose book: ")
		self.display_books()
		a = input("\nEnter Name of book u want:  ")
		b = input("\nEnter your name: ")
		
		self.nav_books.append(a)
		self.av_books.remove(a)
		#--------UPDATING AVAILABILITY-------
		with open("nav.txt", "w") as ff:
			for i in self.nav_books:
				ff.write(f"{i}\n")
		with open("av.txt", "w") as f:
			for it in self.av_books:
				f.write(f"{it}\n")
		#-----------------------------------	
		pr = (f"{a} is given to {b}\n")
		print(pr)
		print("\n ",25*"-")
		with open("lend_books.txt", "a") as f:
			f.write(f"{current} - {pr} \n")
		
	def return_books(self):
		self.aval_books("nav")
		a = input("Name of book u want to return :  ")
		b = input("\nEnter your name: ")		
		self.av_books.append(a)
		self.nav_books.remove(a)
		#--------UPDATING AVAILABILITY-------
		with open("nav.txt", "w") as ff:
			for i in self.nav_books:
				ff.write(f"{i}\n")
		with open("av.txt", "w") as f:
			for it in self.av_books:
				f.write(f"{it}\n")
		#-----------------------------------	
		pr = (f"{a} is returned by {b}\n")
		print(pr)
		print("\n ",25*"-")
		with open("return_books.txt", "a") as f:
			f.write(f"{current} - {pr} \n")
		
	def aval_books(self, aval):
		filen = open("nav.txt")
		nav_books = []
		for book in filen:
			book_snav = book.strip()
			nav_books.append(book_snav)
			
		filea = open("av.txt")
		av_books = []
		for booka in filea:
			book_sav = booka.strip()
			av_books.append(book_sav)
	
		#----------------------->>>	
		if aval=="nav":
			print("\n Issued BOOKS: ")
			for b in nav_books :
				i = "Ã—"
				print(f"{i} {b}")
			print("\n ", 25*"-")
		else :
			print("\n Available BOOKS: ")
			for b in av_books :
				i = "âœ“"
				print(f"{i} {b}")
			print("\n ",25*"-")
			
#out of class

def detail ():
	print(" 1- Display All Books \n","2- Add New Books \n","3- Issuse book For Reader \n","4- Return Book from Reader \n","5- Show available Books \n","6- Show Unavailable Books (Issued) \n ")	
										
#------------Book Data ------------
file = open("books_list.txt")
lists = []
for book in file:
	book_s = book.strip()
	lists.append(book_s)
file.close()		

#-----------Object---------		
				
ilk = Library(lists, "International Library of Knowledge")

#---------------Main code-----------
print("\nInternational Library of India [-Yashraj] \n\n")

while(True):
	detail()
	ch = (input(">>> ")) 
	if ch=="1":
		ilk.display_books()
	elif ch=="2" :
		ilk.add_books()
	elif ch=="3" :
		ilk.lend_books()
	elif ch=="4":
		ilk.return_books()
	elif ch=="5" :
		ilk.aval_books("av")
	elif ch=="6" :
		ilk.aval_books("nav")
	else :
		print("Oops ! Invalid input try again... \n ")
	time.sleep(1)
