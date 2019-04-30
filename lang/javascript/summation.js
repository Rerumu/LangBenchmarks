let v = 0

for (let i = 0; i < 0x40000000; i++) {
	v += i;
}

console.log("Sum: " + v)
