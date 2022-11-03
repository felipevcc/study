// PASSWORDS GENERATOR
 
package main

import (
  "fmt"
  "math/rand"
  "time"
  "strings"
)

func password() string{
  mayus := []string{
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"}
  
  minus := []string{
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"}

  nums := []string{
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

  chars := []string{
    "+", "-", "/", "@", "_", "?", "!", 
    ">", "<", "&", "$", "#"}

  caracteres := append(mayus, minus...)
  caracteres = append(caracteres, nums...)
  caracteres = append(caracteres, chars...)
  
  rand.Seed(time.Now().UnixNano())
  
  pw := []string{}

  for i:=0; i<8; i++ {
    caracter_index := rand.Intn(len(caracteres))
    pw = append(pw, caracteres[caracter_index]) 
  }
  
  return strings.Join(pw, "")

}

func main() {
  fmt.Printf("Su contraseña es: %s\n", password())
}
