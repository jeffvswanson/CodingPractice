package main

import "fmt"

func main() {

	customerNumber := make([]int, 3)
	// 3 is length & capacity
	// length - number of elements referred to by the slice
	// capacity - number of elements in the underlying array
	customerNumber[0] = 7
	customerNumber[1] = 10
	customerNumber[2] = 15

	fmt.Println(customerNumber[0])
	fmt.Println(customerNumber[1])
	fmt.Println(customerNumber[2])

	greeting := make([]string, 3, 5)
	// 3 is length - number of elements referred to by the slice
	// 5 is capacity - number if elements in the underlying array
	// you could also do it like this

	greeting[0] = "Good morning!"
	greeting[1] = "Bonjour!"
	greeting[2] = "dias!"

	fmt.Println(greeting[2])

	/*
	   If we think that our slice might grow, we can set a capacity larger than
	   length. This gives our slice room to grow without golang having to create a
	   new underlying array every time our slice grows. When the slice exceeds
	   capacity, then a new underlying array will be created. These arrays double
	   in size each time they're created (2,4, 8, 16) up to a certain point, and
	   then they scale in a smaller proportion, e.g., 10%.
	*/
}
