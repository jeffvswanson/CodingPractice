package main

import "fmt"

func main() {
	// get the number input
	// print the number divided by two and show the result
	// print whether the number was even or not
	var x int
	fmt.Print("Please enter an integer you want to see divided by two: ")
	fmt.Scan(&x)
	divide := func() {
		var test bool
		if x%2 == 0 {
			test = true
		} else {
			test = false
		}
		fmt.Print(x, "/2 = ", x/2, " and is even: ", test)
	}
	divide()

}

/*
Modify the program from isItEven to use a func expression.
*/
