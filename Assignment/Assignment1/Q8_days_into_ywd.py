##WAP to convert days into years, weeks, and days.

Days = int(input("Enter the days:"))

Years = Days // 365

Days = Days % 365

Weeks = Days // 7

Days = Days % 7

print(f"Years is:{Years}")
print(f"Weeks is:{Weeks}")
print(f"Days is:{Days}")
