package main

import (
	"image"
	"image/color"
	"image/png"
	"log"
	"os"
)

func main() {
	imageFile, err := os.Open("mush.png")
	if err != nil {
		log.Fatal(err)
	}
	defer imageFile.Close()

	loadedImage, err := png.Decode(imageFile)
	if err != nil {
		log.Fatal(err)
	}

	width := loadedImage.Bounds().Max.X
	height := loadedImage.Bounds().Max.Y

	newImage := image.NewNRGBA(image.Rect(0, 0, width, height))

	var pr, pg, pb uint32
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			r, g, b, _ := loadedImage.At(x,y).RGBA()

			r, pr = r ^ pr, r
			g, pg = g ^ pg, g
			b, pb = b ^ pb, b

			newImage.Set(x, y, color.NRGBA{
				R: uint8(r),
				G: uint8(g),
				B: uint8(b),
				A: 255,
			})
		}
	}

	f, err := os.Create("newImage.png")
	if err != nil {
		log.Fatal(err)
	}

	if err := png.Encode(f, newImage); err != nil {
		f.Close()
		log.Fatal(err)
	}

	if err := f.Close(); err != nil {
		log.Fatal(err)
	}
}
