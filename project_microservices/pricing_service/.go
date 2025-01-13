package main

import (
	"encoding/json"
	"net/http"
)

type PriceRequest struct {
	BasePrice float64 `json:"base_price"`
}

type PriceResponse struct {
	Price float64 `json:"price"`
}

func calculatePrice(w http.ResponseWriter, r *http.Request) {
	var req PriceRequest
	json.NewDecoder(r.Body).Decode(&req)

	price := req.BasePrice * 1.15
	res := PriceResponse{Price: price}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(res)
}

func main() {
	http.HandleFunc("/pricing", calculatePrice)
	http.ListenAndServe(":8080", nil)
}
