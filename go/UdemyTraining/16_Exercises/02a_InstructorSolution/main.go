package main

import (
	"fmt"
)

func main() {

	half := func(n int) (int, bool) {
		return n / 2, n%2 == 0
	}

	h, even := half(5)
	fmt.Println(h, even)
}

/*
Modify the program from isItEven to use a func expression.
*/
