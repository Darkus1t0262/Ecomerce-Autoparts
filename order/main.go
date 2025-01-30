package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

const authServiceURL = "http://auth-service:3000/verify"
const productServiceURL = "http://product-service:4000/graphql"

// Verify JWT with auth-service
func verifyToken(token string) bool {
	req, _ := http.NewRequest("GET", authServiceURL, nil)
	req.Header.Set("Authorization", token)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil || resp.StatusCode != http.StatusOK {
		return false
	}
	return true
}

// Query product availability from product-service
func checkProductAvailability(productID string) bool {
	query := fmt.Sprintf(`{"query": "{ products { id name price } }"}`)
	req, _ := http.NewRequest("POST", productServiceURL, ioutil.NopCloser([]byte(query)))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil || resp.StatusCode != http.StatusOK {
		return false
	}

	body, _ := ioutil.ReadAll(resp.Body)
	var response map[string]interface{}
	json.Unmarshal(body, &response)

	for _, product := range response["data"].(map[string]interface{})["products"].([]interface{}) {
		if product.(map[string]interface{})["id"] == productID {
			return true
		}
	}
	return false
}

// Order processing endpoint
func orderHandler(w http.ResponseWriter, r *http.Request) {
	token := r.Header.Get("Authorization")
	if !verifyToken(token) {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}

	productID := r.URL.Query().Get("product_id")
	if !checkProductAvailability(productID) {
		http.Error(w, "Product not available", http.StatusNotFound)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"message": "Order placed successfully!"}`))
}

func main() {
	http.HandleFunc("/order", orderHandler)

	fmt.Println("Order Service running on port 5000")
	log.Fatal(http.ListenAndServe(":5000", nil))
}
