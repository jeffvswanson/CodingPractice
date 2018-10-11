package main

import (
	"fmt"
)

func main() {
	c := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			c <- i
		}
	}()

	for {
		fmt.Println(<-c)
	}

}

// This prints the number, but we have received this error:
// fatal error: all goroutines are asleep - deadlock!
// Where is the deadlock?
// Why are all the goroutines asleep?
// How can we fix this?

// The deadlock is at the Println(<-c) for loop. The loop is waiting for
// another value from the channel, but the channel is not producing any more
// values. So, the for loop has become an infinite loop while the channel is
// quiet.
// We can fix this by iterating over the range of the channel directly
// instead of using an infinite loop.
