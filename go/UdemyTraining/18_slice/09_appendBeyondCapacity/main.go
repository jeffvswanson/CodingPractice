package main

import "fmt"

func main() {

	greeting := make([]string, 3, 5)
	// 3 is length - number of elements referred to by the slice
	// 5 is capacity - number of elements in the underlying array

	greeting[0] = "Good morning!"
	greeting[1] = "Bonjour!"
	greeting[2] = "buenos dias!"
	greeting = append(greeting, "Suprabadham")
	greeting = append(greeting, "Zao'an")
	greeting = append(greeting, "Ohayou gozaimasu")
	greeting = append(greeting, "gidday")

	fmt.Println(greeting[6])
	fmt.Println(len(greeting))
	fmt.Println(cap(greeting))

	/*
	   If we think that our slice might grow, we can set a capacity larger than
	   length. This gives our slice room to grow without golang having to create a
	   new underlying array every time our slice grows. When the slice exceeds
	   capacity, then a new underlying array will be created. These arrays double
	   in size each time they're created (2,4, 8, 16) up to a certain point, and
	   then they scale in a smaller proportion, e.g., 10%.
	*/
}
