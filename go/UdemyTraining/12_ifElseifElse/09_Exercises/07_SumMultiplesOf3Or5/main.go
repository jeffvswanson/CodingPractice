package main

import "fmt"

func main() {
	var sum int
	sum = 0
	for i := 1; i < 1000; i++ {
		if i%3 == 0 {
			sum = sum + i
		} else if i%5 == 0 {
			sum = sum + i
		}
	}
	fmt.Println("The sum of the numbers less than")
	fmt.Println("1000 divisible by 3 and 5 is:", sum)
}
