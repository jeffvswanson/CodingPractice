package main

import (
	"fmt"
	"strconv"
	"sync"
)

func main() {
	c1 := incrementor("1")
	c2 := incrementor("2")
	var count int
	for n := range merge(c1, c2) {
		fmt.Println(n)
		count++
	}
	fmt.Println("Final Counter:", count)
}

func incrementor(s string) <-chan string {
	out := make(chan string)
	go func() {
		for i := 0; i < 20; i++ {
			str := "Process: " + s + " printing: " + strconv.Itoa(i)
			out <- str
		}
		close(out)
	}()
	return (out)
}

func merge(cs ...<-chan string) chan string {
	out := make(chan string)
	var wg sync.WaitGroup

	output := func(c <-chan string) {
		for n := range c {
			out <- n
		}
		wg.Done()
	}

	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}

	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

/*
CHALLENGE - COMPLETE!
-- Take the code from above and change it to use channels instead of wait
groups and atomicity.
*/
