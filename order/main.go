package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	"context"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var authServiceURL = os.Getenv("AUTH_SERVICE_URL")       // e.g., http://auth-service:3000
var productServiceURL = os.Getenv("PRODUCT_SERVICE_URL") // e.g., http://product-service:4000/graphql
var mongoURI = os.Getenv("MONGO_URI")                    // Ensure it's loading correctly admin:password@mongo-db:27017
var mongoDBName = os.Getenv("MONGO_DB_NAME")             // e.g., orders_db

var db *mongo.Database

// Connect to MongoDB
func connectDB() {
	clientOptions := options.Client().ApplyURI(mongoURI)
	client, err := mongo.Connect(context.TODO(), clientOptions)
	if err != nil {
		log.Fatalf("❌ MongoDB Connection Error: %v", err)
	}
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		log.Fatalf("❌ MongoDB Ping Error: %v", err)
	}
	db = client.Database(mongoDBName)
	fmt.Println("✅ Connected to MongoDB - Order Service")
}

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
	query := `{"query": "{ products { id name price } }"}`
	req, _ := http.NewRequest("POST", productServiceURL, bytes.NewBuffer([]byte(query)))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil || resp.StatusCode != http.StatusOK {
		return false
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body) // FIXED: Replace ioutil.ReadAll with io.ReadAll
	var response map[string]interface{}
	err = json.Unmarshal(body, &response)
	if err != nil {
		log.Println("❌ JSON Parse Error:", err)
		return false
	}

	products, ok := response["data"].(map[string]interface{})["products"].([]interface{})
	if !ok {
		log.Println("❌ Invalid response format from product-service")
		return false
	}

	for _, p := range products {
		product := p.(map[string]interface{})
		if fmt.Sprintf("%v", product["id"]) == productID {
			return true
		}
	}
	return false
}

// Save order in MongoDB
func saveOrder(productID, customer string, quantity int) error {
	collection := db.Collection("orders")
	order := bson.M{
		"product_id": productID,
		"customer":   customer,
		"quantity":   quantity,
		"status":     "Pending",
		"created_at": time.Now(),
	}

	_, err := collection.InsertOne(context.TODO(), order)
	return err
}

// Order processing endpoint
func orderHandler(w http.ResponseWriter, r *http.Request) {
	token := r.Header.Get("Authorization")
	if !verifyToken(token) {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}

	productID := r.URL.Query().Get("product_id")
	customer := r.URL.Query().Get("customer")
	quantity := r.URL.Query().Get("quantity")

	if productID == "" || customer == "" || quantity == "" {
		http.Error(w, "Missing required parameters", http.StatusBadRequest)
		return
	}

	if !checkProductAvailability(productID) {
		http.Error(w, "Product not available", http.StatusNotFound)
		return
	}

	err := saveOrder(productID, customer, 1) // Defaulting quantity to 1 for now
	if err != nil {
		http.Error(w, "Failed to save order", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"message": "✅ Order placed successfully!"}`))
}

func main() {
	connectDB() // Connect to MongoDB

	http.HandleFunc("/order", orderHandler)

	fmt.Println("✅ Order Service running on port 5000")
	log.Fatal(http.ListenAndServe(":5000", nil))
}
