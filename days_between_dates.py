"""
	A handy dandy python script to count the number of days between two given dates.
	Also counts the number of times each day appears.
"""

from datetime import date

days_list: tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def count_days(d1: date, d2: date) -> dict:
	"""Count the number of times each day appears between two dates."""
	
	days_counter: dict = {day: 0 for day in days_list}
	for ord_date in range(d1.toordinal(), d2.toordinal()):
		d: date = date.fromordinal(ord_date)
		days_counter[days_list[d.weekday()]] += 1
	
	return days_counter

if __name__ == "__main__":
	def get_date_as_input(message: str) -> date:
		"""Get user input and convert it to a valid date object."""
		
		while True:
			inp: str = input(message).strip()
			if inp.lower() == 'today':
				return date.today()
			inp: str = inp.split()
			
			try:
				year: int = int(inp[0])
				month: int = int(inp[1])
				day: int = int(inp[2])
				input_date: date = date(year, month, day)
				return input_date
			except (TypeError, IndexError, ValueError):
				print("[ERROR] Invalid date format, try again.\n")
				continue

	print('Enter dates in the format "YYYY MM DD". Eg: "2020 12 28" (without quotes).', '\n')
	date1: date = get_date_as_input("Starting Date: ")
	date2: date = get_date_as_input("Ending Date: ")
		
	days_counted: dict = count_days(date1, date2)
	print()
	print(f"Days between {date1.strftime('%B %d, %Y')} and {date2.strftime('%B %d, %Y')}\n")
	print(f"Total Days: {sum(days_counted.values())}\n")
	for day, count in days_counted.items():
		print(f"{day}s: {count}")
	input()