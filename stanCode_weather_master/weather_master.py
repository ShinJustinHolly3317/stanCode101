"""
File: weather_master.py
Name: Justin Kao
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

ENDING = -99


def main():
	"""
	Use While loop to keep comparing input temperature is bigger or smaller than the maximum and minimum.
		If bigger, replace maximum with the new input.
		If smaller, replace minimum with the new input.
		Use a counter(day) to add up total days.
	"""
	print("stanCode \"weather Master 4.0 \"")
	data = float(input("Next temperature: (or " + str(ENDING) + " to quit)? "))
	if data == ENDING:
		print("No Temperatures were entered!")
	else:
		maximum = data
		minimum = data
		total = 0
		days = 0
		cold_days = 0
		while True:
			if data == ENDING:  # leave loop
				break
			elif data > maximum:  # beat previous maximum
				maximum = data
			elif data < minimum:  # beat previous minimum
				minimum = data
			if data < 16:  # must do if statement
				cold_days += 1
			total += data
			days += 1
			data = float(input("Next temperature: (or " + str(ENDING) + " to quit)? "))
		avg = total / days

		print("-----------------------------------------")
		print("Highest Temperature: " + str(maximum))
		print("Lowest Temperature: " + str(minimum))
		print("Average Temperature: " + str(avg))
		print(str(cold_days) + " cold days")



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
