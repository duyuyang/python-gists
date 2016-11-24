# --- AND ---

a = 50     # 110010
b = 25     # 011001
c = a & b  # 010000

print c

# --- RIGHT SHIFT ---
x = 240     # 11110000
y = x >> 2  # 00111100

print y

# --- Bitwise Exclusive ---
# -- same 0, diff 1
x = 15
y = 15 ^ 4

print y

# --- Bitwise Inversion ---
x = 15
y = ~ x

# --- or ---
x = 15
y = 20

print x | y


#cost = map(float, [raw_input(), raw_input(), raw_input()])
#print cost[0] + cost[0]*cost[1]/100 + cost[0]*cost[2]/100

cost = float(raw_input())
percent = map(float, [100, raw_input(), raw_input()])
print round(sum(map(lambda x: cost*x/100, percent)))
