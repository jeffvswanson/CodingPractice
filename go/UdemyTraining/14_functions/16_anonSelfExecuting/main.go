package main

import "fmt"

func main() {
	func() {
		fmt.Println("I'm driving!")
	}() // Parantheses are needed to execute the anonymous function
}
