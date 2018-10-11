package main

import "fmt"

type foo int

func main() {
	var myAge foo
	myAge = 44
	fmt.Printf("%T %v \n", myAge, myAge)

	var yourAge int
	yourAge = 33
	fmt.Printf("%T, %v \n", yourAge, yourAge)

	// This does not work:
	// fmt.Println(myAge + yourAge)

	// This conversion works:
	// fmt.Println(int(myAge) + yourAge)
}
