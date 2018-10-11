package main

import (
	"fmt"
)

func main() {
	c := make(chan int)

	go func() {
		c <- 1
		close(c)
	}()

	fmt.Println(<-c)
}

// This results in a deadlock.
// Can you determine why?
// And what would you do to fix it?

// The channel is never opened in a go function.
// Create an anonymous self-executing go function, close the channel,
// and allow main to pull the value off the channel to prevent the package
// from closing prematurely.
