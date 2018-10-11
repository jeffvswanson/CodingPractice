package main

import "fmt"

func main() {
	var small uint64
	var large uint64

	fmt.Print("Please enter a number: ")
	fmt.Scan(&small)
	fmt.Print("Please enter a larger number: ")
	fmt.Scan(&large)

	for large <= small {
		fmt.Println(large, " is less than or equal to ", small)
		fmt.Println("You need to enter a larger number!")
		fmt.Print("Please enter a larger number: ")
		fmt.Scan(&large)
	}

	fmt.Println("The remainder of the larger number divided by ")
	fmt.Println("the smaller number is:", large%small)

}
