package main

import "fmt"

type vehicle struct {
	Seats    int
	Maxspeed int
	Color    string
}

type car struct {
	vehicle
	wheels int
	Doors  int
}

type plane struct {
	vehicle
	Jet bool
}

type boat struct {
	vehicle
	Length int
}

func (v vehicle) Specs() {
	fmt.Printf("Seats %v, max speed %v, color %v\n", v.Seats, v.Maxspeed, v.Color)
}

func main() {
	prius := car{}
	tacoma := car{}
	bmw528 := car{}
	cars := []car{prius, tacoma, bmw528}

	boeing747 := plane{}
	boeing757 := plane{}
	boeing767 := plane{}
	planes := []plane{boeing747, boeing757, boeing767}

	sanger := boat{}
	nautique := boat{}
	malibu := boat{}
	boats := []boat{sanger, nautique, malibu}

	for key, value := range cars {
		fmt.Println(key, " - ", value)
	}

	for key, value := range planes {
		fmt.Println(key, " - ", value)
	}

	for key, value := range boats {
		fmt.Println(key, " - ", value)
	}
}
