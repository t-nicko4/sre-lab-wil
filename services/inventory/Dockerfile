
# syntax=docker/dockerfile:1
FROM golang:1.22-alpine AS build
WORKDIR /src
COPY go.mod ./
RUN go mod download
COPY . .
RUN go build -o /bin/inventory main.go

FROM alpine:3.20
WORKDIR /app
COPY --from=build /bin/inventory /app/inventory
EXPOSE 8002
CMD ["/app/inventory"]