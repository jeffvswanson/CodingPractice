package main

import "fmt"

type vehicles interface{}

type vehicle struct {
	Seats    int
	Maxspeed int
	Color    string
}

type car struct {
	vehicle
	wheels int
	doors  int
}

type plane struct {
	vehicle
	jet bool
}

type boat struct {
	vehicle
	length int
}

func (v vehicle) Specs() {
	fmt.Printf("Seats %v, max speed %v, color %v\n", v.Seats, v.Maxspeed, v.Color)
}

func main() {
	prius := car{}
	tacoma := car{}
	bmw528 := car{}
	boeing747 := plane{}
	boeing757 := plane{}
	boeing767 := plane{}
	sanger := boat{}
	nautique := boat{}
	malibu := boat{}
	rides := []vehicles{prius, tacoma, bmw528, boeing747, boeing757, boeing767, sanger, nautique, malibu}

	for key, value := range rides {
		fmt.Println(key, " - ", value)
	}
}
