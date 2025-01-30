FROM golang:1.19

WORKDIR /app

# Copy module files first and tidy dependencies
COPY go.mod go.sum ./
RUN go mod tidy

# Copy the rest of the application files
COPY . .

# Build the Go application
RUN go build -o main .

CMD ["./main"]
