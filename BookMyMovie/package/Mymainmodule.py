class Cinema:
	list1=[]
	while True:
			print("Enter the number of rows:")
			no_of_rows=input()
			print("Enter the number of seats in each row:")
			no_of_seat=input()
			if no_of_rows.isdigit()==False or no_of_seat.isdigit()==False:
				print("\nEnter the correct input in numbers\n")
			else:
					no_of_rows=int(no_of_rows)
					no_of_seat=int(no_of_seat)
					break
	total_ticket=no_of_rows*no_of_seat
	no_of_ticket_sold=len(list1)
	current_income=0
	total_income=0
					
	def menu(self):
					
		while True:
			print("\n1. Show the seats")
			print("2. Buy a ticket")
			print("3. Statistics")
			print("4. Show booked Ticket User Info")
			print("0. Exit")
			User_input=input()
			if User_input=="0":
				break
			elif User_input=="1":
				self.show_the_seat()
			elif User_input=="2":
				self.buy_ticket()
			elif User_input=="3":
				self.statistics()
			elif User_input=="4":
				self.User_info()
			else:
				print("Invalid Input")
				
	def show_the_seat(self):
		print("\nCinema:\n"," ",end="")
		for i in range(1,Cinema.no_of_seat+1):
			print(i,end=" ")

		for i in range(1,Cinema.no_of_rows+1):
			print("\n",end="")
			print(i,end=" ")
			for j in range(1,Cinema.no_of_seat+1):
				print(Cinema.Seatshow(i,j),end=" ")
		print("\n")
		
	def buy_ticket(self):
		while True:
			print("\nEnter the row number for the ticket")
			row_number=input()
			if row_number.isdigit() and int(row_number) in range(1,Cinema.no_of_rows+1):
				row_number=int(row_number)
				break
			else:
				print("Please Enter the row number correctly")
		
		while True:
			print("Enter the column number for the ticket")
			column_number=input()
			if column_number.isdigit() and int(column_number) in range(1,Cinema.no_of_seat+1):
				column_number=int(column_number)
				break
			else:
				print("Please Enter the column number correctly")
				
		y=Cinema.showprice(Cinema.no_of_rows,Cinema.no_of_seat,row_number)
		print(f"\nTicket Price: ${y}","\nYou want to book")
		print("\n1. Yes\n2. No")
		choice=input()
		if choice =="1":
			Cinema.current_income+=y
			self.detail=Cinema.fill_detail(row_number,column_number,y)
			Cinema.list1.append(self.detail)
		elif choice=="2":
			print("\n")	
				
	def statistics(self):
		print("\nNumber of purchased tickets: ",Cinema.no_of_ticket_sold())
		print(f"Percentage: {Cinema.sold_percentage()}%")
		print("Current Income: $"+str(Cinema.current_income))
		print("Total Income: $"+str(Cinema.total_income))
		
	def User_info(self):
		while True:
			print("\nEnter the row number ")
			row_num=input()
			if row_num.isdigit() and int(row_num) in range(1,Cinema.no_of_rows+1):
				row_num=int(row_num)
				break
			else:
				print("Please Enter the row number correctly")
		
		while True:
			print("Enter the column number")
			column_num=input()
			if column_num.isdigit() and int(column_num) in range(1,Cinema.no_of_seat+1):
				column_num=int(column_num)
				break
			else:
				print("Please Enter the column number correctly")
				
		for obj1 in Cinema.list1:
			if obj1["Row Number"]==row_num and obj1["Column Number"]==column_num:
				print("\nName:",obj1["Name"] )
				print("Gender:",obj1["Gender"])
				print("Age:",obj1["Age"])
				print("Ticket Price:",obj1["Ticket Price"])
				print("Phone Number:",obj1["Phone Number"])
				break
			
		else:
				print("This seat is vaccant")
				
	@classmethod
	def sold_percentage(cls):
			return round((cls.no_of_ticket_sold()/cls.total_ticket)*100,2)
			
	@classmethod
	def no_of_ticket_sold(cls):
			return len(cls.list1)						
								
	@staticmethod
	def fill_detail(r,c,z):
			print("\nEnter your Name")
			name=input()
			print("\nChoose your gender\n\nMale\nFemale\nOther\n")
			gender=input()
			print("\nEnter your age")
			age=input()
			print("\nEnter your phone number")
			phone_number=input()
			print("\nBooked Successfully")
			return {"Name":name,"Gender":gender,"Age":age,"Phone Number": phone_number,"Row Number":r,"Column Number":c,"Ticket Price":f"{z}$"}
			
	@staticmethod
	def showprice(rows,seats,choice_of_row):
		if Cinema.total_ticket<60:
			Cinema.total_income =Cinema.total_ticket*10
			return 10
		else:
			half_rows=rows//2
			Cinema.total_income=half_rows*Cinema.no_of_seat*10+(Cinema.no_of_rows-half_rows)*Cinema.no_of_seat*8
			if choice_of_row>half_rows:
				return 8
			else:
				return 10
				
	@staticmethod
	def Seatshow(r,c):
		for obj in Cinema.list1:
			if obj["Row Number"]==r and obj["Column Number"]==c:
				return "B"
		else:
			return "S"

S=Cinema()
S.menu()