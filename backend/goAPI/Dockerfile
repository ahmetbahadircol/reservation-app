FROM golang:1.23

WORKDIR /src

# Pre-copy go.mod and go.sum to leverage Docker cache for dependencies
COPY go.mod go.sum ./
RUN go mod download && go mod verify

# Copy the source code into the container
COPY . .

# Ensure the output directory exists and build the Go binary
RUN go build -v -o /usr/local/bin/app ./main.go

# Set the default command to run the binary
CMD ["/usr/local/bin/app"]
