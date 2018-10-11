package main

import "fmt"

func main() {
	// get the number input
	// print the number divided by two and show the result
	// print whether the number was even or not
	var x int
	fmt.Print("Please enter an integer you want to see divided by two: ")
	fmt.Scan(&x)
	fmt.Print(x, "/2 = ")
	fmt.Print(divide(x))
}

func divide(x int) (int, bool) {
	var test bool
	if x%2 == 0 {
		test = true
	} else {
		test = false
	}
	return (x / 2), test
}

/*
Write a function which takes an integer. The function will have two returns.
The first return should be the argument divided by 2. The second return
should be a bool that let's us know whether or not the argument was even.
For example:
	a. half(1) returns (0, false)
	b. half(2) returns (1, true)
*/
