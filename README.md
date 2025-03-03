docker build -t fast-alrp -f Dockerfile .
docker run -it -d --name fast-alrp -p 8000:8000  fast-alrp:latest


curl -X POST -F "file=@car1.jpg" http://localhost:8000/
