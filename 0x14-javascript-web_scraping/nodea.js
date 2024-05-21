#!/usr/bin/node

const dicti = { '1': 11,
	       '2': 8,
	       '3': 7,
	       '4': 6,
	       '5': 12,
	       '6': 0,
	       '7': 9,
	       '8': 11,
	       '9': 8,
	       '10': 12 };
console.log(typeof(dicti));
for (const [key, value] of Object.entries(dicti)) {
    if (value == 0) {
	delete(dicti[key]);
    }
}

console.log(dicti);
