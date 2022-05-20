# Expected output "module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04"
t = (0, 4, 132.42222, 10000, 12345.67)
output = f"module_{t[0]:#02}, ex_{t[1]:#02} "
output += f": {t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}"
print(output)
