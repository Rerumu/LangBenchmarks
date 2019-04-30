local var = 0

for i = 1, 0x40000000 do
	var = var + i
end

print('Sum: ' .. var)
