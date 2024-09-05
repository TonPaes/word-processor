# word-processor

## Documentation

```bash 
localhost:<port>/docs
```
live version:

https://ton-word-processor-794d5ae9be6c.herokuapp.com/docs#/

## Project Setup

To set up the project environment, follow these steps:

1. Clone the repository:  

```bash 
git clone https://github.com/TonPaes/word-processor
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a virtual environment:

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **Linux & MacOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Running
```bash
uvicorn main:app --reload
```

### Containerized deployment 

Build the Docker image by running the following command:

```bash
docker build -t your-image-name .
```
Once the image is built, you can run a Docker container based on that image using the following command:

```bash
docker run -d -p host-port:container-port your-image-name
```
