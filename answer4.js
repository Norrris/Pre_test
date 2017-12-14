function createArrayOfFunctions(y) {
var arr = [];
for(var i = 0; i<y; i++) {
	// as loop cannot store functions, I change it to store the function as string when input the value of y.
arr[i] = "function(x) { return x + "+i+"; }";
}
return arr;
}