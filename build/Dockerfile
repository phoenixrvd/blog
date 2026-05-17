FROM cgr.dev/chainguard/nginx:latest

WORKDIR /usr/share/nginx/html

# Static site files are expected in build/dist
COPY dist/ ./

EXPOSE 8080
