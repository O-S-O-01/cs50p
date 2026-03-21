def main():
	months =['January', 'February', 'March', 'April', 'May', 'june', 'July', 'August', 'September', 'October', 
			'November', 'December']
	while True:
		try:
			date = input ('what is the date: ').strip()
			if '/' in date:
				month, day, year = date.split('/')
				month= int(month)
				day= int(day)
				year= int(year)
			else:
				parts = date.split(' ')
				month_str=parts[0]
				day=parts[1].replace(',','')
				year=parts[2]
				
				if month_str not in months:
					raise ValueError
				month = month.index(month_str)+1
				day = int(day)
				year=int(year)
			if day<1 or day >31:
				raise ValueError
			print (f'{year}-{month:02}-{day:02}')
			break
		
		except (ValueError, IndexError):
			continue
if __name__ == '__main__':
	main()
