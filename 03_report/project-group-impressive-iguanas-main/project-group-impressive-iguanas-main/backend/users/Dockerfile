# syntax=docker/dockerfile:1
# docker build --no-cache --progress=plain --tag users .

FROM golang:1.19

# Set destination for COPY
WORKDIR /app

# Download Go modules
COPY go.mod go.sum ./
RUN go mod download

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/engine/reference/builder/#copy
COPY cmd ./cmd
COPY pkg ./pkg

RUN echo $(ls -1 ./)
RUN echo $(ls -1 ./pkg/)
RUN echo $(ls -1 ./pkg/login)

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /users ./cmd


# To bind to a TCP port, runtime parameters must be supplied to the docker command.
# But we can (optionally) document in the Dockerfile what ports
# the application is going to listen on by default.
# https://docs.docker.com/engine/reference/builder/#expose
EXPOSE 8080

# Run
CMD [ "/users" ]
