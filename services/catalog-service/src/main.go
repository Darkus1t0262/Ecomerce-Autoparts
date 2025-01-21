package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/graphql-go/graphql"
)

// Product defines the structure for the catalog items
type Product struct {
	ID    int     `json:"id"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}

// Mock data for the catalog
var products = []Product{
	{ID: 1, Name: "Oil Filter", Price: 20.50},
	{ID: 2, Name: "Car Battery", Price: 120.00},
	{ID: 3, Name: "Brake Pads", Price: 35.75},
}

// Define GraphQL Schema
var productType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Product",
	Fields: graphql.Fields{
		"id": &graphql.Field{
			Type: graphql.Int,
		},
		"name": &graphql.Field{
			Type: graphql.String,
		},
		"price": &graphql.Field{
			Type: graphql.Float,
		},
	},
})

var rootQuery = graphql.NewObject(graphql.ObjectConfig{
	Name: "Query",
	Fields: graphql.Fields{
		"products": &graphql.Field{
			Type: graphql.NewList(productType),
			Resolve: func(p graphql.ResolveParams) (interface{}, error) {
				return products, nil
			},
		},
		"product": &graphql.Field{
			Type: productType,
			Args: graphql.FieldConfigArgument{
				"id": &graphql.ArgumentConfig{
					Type: graphql.Int,
				},
			},
			Resolve: func(p graphql.ResolveParams) (interface{}, error) {
				id, ok := p.Args["id"].(int)
				if ok {
					for _, product := range products {
						if product.ID == id {
							return product, nil
						}
					}
				}
				return nil, fmt.Errorf("product not found")
			},
		},
	},
})

var schema, _ = graphql.NewSchema(graphql.SchemaConfig{
	Query: rootQuery,
})

// GraphQL handler
func graphqlHandler(w http.ResponseWriter, r *http.Request) {
	var params struct {
		Query string `json:"query"`
	}
	if err := json.NewDecoder(r.Body).Decode(&params); err != nil {
		http.Error(w, "Invalid request payload", http.StatusBadRequest)
		return
	}

	result := graphql.Do(graphql.Params{
		Schema:        schema,
		RequestString: params.Query,
	})
	if len(result.Errors) > 0 {
		http.Error(w, fmt.Sprintf("GraphQL errors: %v", result.Errors), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(result)
}

func main() {
	r := chi.NewRouter()
	r.Post("/graphql", graphqlHandler)

	fmt.Println("Catalog Service running at http://localhost:8080/graphql")
	http.ListenAndServe(":8080", r)
}
