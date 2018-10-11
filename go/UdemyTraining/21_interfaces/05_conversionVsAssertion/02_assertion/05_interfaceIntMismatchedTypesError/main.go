package main

import "fmt"

func main() {
	var val interface{} = 7
	fmt.Println(val + 6) //purposeful error, you must assert the interface
	// val.(int) for this to work
}
