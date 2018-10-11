package main

import (
	"fmt"
	"log"
)

type NorgateMathError struct {
	lat, long string
	err       error
}

func (n *NorgateMathError) Error() string {
	return fmt.Sprintf("a norgate math error occurred: %v %v %v",
		n.lat, n.long, n.err)
}

func main() {
	_, err := sqrt(-10)
	if err != nil {
		log.Fatalln(err)
	}
}

func sqrt(f float64) (float64, error) {
	if f < 0 {
		// Error variable put inside the function to have access to f.
		nme := fmt.
			Errorf(
				"norgate math again: square root of a negative number : %v",
				f)
		return 0, &NorgateMathError{"50.2289 N", "99.4656 W", nme}
	}
	//implementation
	return 42, nil
}
