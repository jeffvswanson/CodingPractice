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
		close(c)
	}()

	for n := range c {
		fmt.Println(n)
	}

}

// Why does this only print zero?
// And what can you to to get it to print all 0 - 9 numbers?

// This only prints to zero because the channel does not have anything
// recieving the value written to the channel. My solution is to move
// close the channel and iterate across the channel.
