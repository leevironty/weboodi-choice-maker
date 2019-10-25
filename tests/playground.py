from weboodi.period import Period

print("setup starting")
p = Period()

courses = "MS-C2111, MS-C2128, CS-C3160".split(", ")
blocks = "pe 8.15-10.00, to 12.15-14.00, ti 10.15-12.00".split(", ")
for c in courses:
    p.add_course_by_code(c)
for b in blocks:
    p.add_block_to_calendar(b)
print("setup done")