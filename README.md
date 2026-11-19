# 🐱 Random Fact Generator

A simple Python-based project that fetches interesting random animal facts using the **Cat Facts API**. The application uses the Python `requests` library to send an HTTP GET request, process the JSON response, and display a random animal fact.

The project is also containerized using **Docker**, making it easy to build and run in an isolated environment.

## 🚀 Features

- Fetches random animal facts from an external REST API.
- Uses Python Requests for API communication.
- Processes JSON API responses.
- Displays the random fact in a readable format.
- Dockerized for easy deployment and execution.

## 🛠️ Technologies Used

- Python 3.9
- Requests Library
- REST API
- Docker
- Git & GitHub

## 📂 Project Structure

```text
Random_Fact_Generator_Cat/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/Ansh1gupta/Random_Fact_Generator_Cat.git
```

**2. Navigate to the project directory**

```bash
cd Random_Fact_Generator_Cat
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python app.py
```

## 🐳 Run Using Docker

**1. Build the Docker image**

```bash
docker build -t random-fact-generator .
```

**2. Run the Docker container**

```bash
docker run --rm random-fact-generator
```

## 🌐 API Used

**Cat Facts API:** https://catfact.ninja/fact

This API provides random cat facts in JSON format.

## 📸 Sample Output

```text
Status Code: 200

🐱 Random Animal Fact:
Cats have five toes on their front paws.
```

*Note: The displayed fact will vary each time the application runs.*

## 🎯 Learning Outcomes

- Understanding how REST APIs work.
- Sending HTTP requests using Python.
- Handling JSON responses.
- Creating and running Docker images and containers.
- Learning basic Git and GitHub workflows.

## 👨‍💻 Author

**Ansh Gupta**

GitHub: [Ansh1gupta](https://github.com/Ansh1gupta)

---

⭐ If you find this project useful, feel free to star the repository!
