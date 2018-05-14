import math, prettytable
table = prettytable.PrettyTable()

def to_rad(angle_deg):
	angle_rad = math.sin((angle_deg * math.pi) / 180)
	return round(angle_rad, 4)

table.field_names = ["Degrees", "Radians"]

i = 0
while i <= 360:
	table.add_row([i, to_rad(i)])
	i += 15	
table.align = "l"
print(table)
