package main

import (
    "fmt"
    "log"
    "net/http"
    "github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
    CheckOrigin: func(r *http.Request) bool { return true },
}

func handleWebSocket(w http.ResponseWriter, r *http.Request) {
    conn, err := upgrader.Upgrade(w, r, nil)
    if err != nil {
        log.Println("WebSocket upgrade error:", err)
        return
    }
    defer conn.Close()
    
    for {
        messageType, p, err := conn.ReadMessage()
        if err != nil {
            log.Println("Read error:", err)
            return
        }
        log.Printf("Received: %s", p)
        conn.WriteMessage(messageType, []byte("Order received!"))
    }
}

func main() {
    http.HandleFunc("/ws", handleWebSocket)
    fmt.Println("Order Service running on port 5000")
    log.Fatal(http.ListenAndServe(":5000", nil))
}