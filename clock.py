import sympy

MHz = 1000*1000

# TX
dev_d87 = sympy.Symbol("d87")
dev_9ce = sympy.Symbol("9ce")

# RX
dev_f24 = sympy.Symbol("f24")
dev_3a0 = sympy.Symbol("3a0")

res = sympy.solve([
	dev_d87 + dev_f24 - (5*MHz)/3000, # 時計回り、一秒あたり回転数
	dev_d87 + dev_3a0 + (5*MHz)/42000, # 半時計回り
	dev_9ce + dev_f24 + (5*MHz)/2400,
	# dev_9ce + dev_3a0 + (5*MHz)/1200
], dev_f24)
print(res)