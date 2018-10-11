package main

import "fmt"

func main() {

	myGreeting := make(map[string]string)
	myGreeting["Tim"] = "Good morning."
	myGreeting["Jenny"] = "Bonjour."

	myGreeting["Harleen"] = "Howdy"
	fmt.Println(myGreeting)
	myGreeting["Harleen"] = "Gidday"
	fmt.Println(myGreeting)
}
