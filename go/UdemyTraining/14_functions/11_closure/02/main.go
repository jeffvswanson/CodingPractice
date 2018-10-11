package main

import "fmt"

var x int

func increment() int {
	x++
	return x
}

func main() {
	fmt.Println(increment())
	fmt.Println(increment())
}

/*
Closure helps us limit the scope of the variables used by multiple functions
without closure, for tow or more funcs to have access to the same variable,
that variable would need to be package scope.
*/
