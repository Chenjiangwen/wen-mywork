# syntax=docker/dockerfile:1
FROM golang:1.19

# Set destination for COPY
WORKDIR /app

# Download Go modules
COPY go.mod go.sum ./
RUN go mod download

# Copy the source code
COPY cmd ./cmd
COPY pkg ./pkg

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /featureflag ./cmd

# To bind to a TCP port, runtime parameters must be supplied to the docker command.
# https://docs.docker.com/engine/reference/builder/#expose
EXPOSE 8080

# Run
CMD [ "/featureflag" ]
