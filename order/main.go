package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var authServiceURL = os.Getenv("AUTH_SERVICE_URL")
var productServiceURL = os.Getenv("PRODUCT_SERVICE_URL")
var mongoURI = os.Getenv("MONGO_URI")
var mongoDBName = os.Getenv("MONGO_DB_NAME")

var db *mongo.Database

func connectDB() {
	clientOptions := options.Client().ApplyURI(mongoURI).SetAuth(options.Credential{
		Username: os.Getenv("MONGO_USER"),
		Password: os.Getenv("MONGO_PASSWORD"),
	})

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

func verifyToken(token string) bool {
	req, _ := http.NewRequest("GET", authServiceURL+"/verify", nil)
	req.Header.Set("Authorization", token)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil || resp.StatusCode != http.StatusOK {
		return false
	}
	return true
}

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

	err := saveOrder(productID, customer, 1)
	if err != nil {
		http.Error(w, "Failed to save order", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"message": "✅ Order placed successfully!"}`))
}

func main() {
	connectDB()

	http.HandleFunc("/order", orderHandler)

	fmt.Println("✅ Order Service running on port 5000")
	log.Fatal(http.ListenAndServe(":5000", nil))
}
