package main

import (
	"fmt"
	"strings"
)

func main() {
	wishlist := "tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol"
	fmt.Println(wishlist)
	r := []rune(wishlist)

	var builder1 strings.Builder

	for i := len(r) - 3; i >= 0; i-=3 {
		m := string(r[i:i+3])
		builder1.WriteString(m)
	}

	wishlist2 := builder1.String()
	fmt.Println(wishlist2)

	var builder2 strings.Builder

	for i := 0; i < len(wishlist2); i+=2 {
		first := string(wishlist2[i])
		second := string(wishlist2[i+1])
		builder2.WriteString(second)
		builder2.WriteString(first)
	}

	wishlist3 := builder2.String()
	fmt.Println(wishlist3)

	final := wishlist3[len(wishlist3)/2:] + wishlist3[:len(wishlist3)/2]
	fmt.Println(final)
}
