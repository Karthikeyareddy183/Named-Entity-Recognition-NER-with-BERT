# Named-Entity-Recognition-NER-with-BERT
This project demonstrates how to fine-tune a BERT model for Named Entity Recognition (NER) using the CoNLL-2003 dataset and deploy it as a Flask API with a web interface. The application is containerized using Docker for easy deployment.

**Features**
  -Fine-tuned BERT model for NER.
  -Flask API with a /predict endpoint for JSON input.
  -Web interface for interactive NER predictions.
  -Basic authentication for API access.
  -Dockerized for easy deployment.

**Technologies Used**
  -Python: Programming language.
  -Flask: Web framework for the API.
  -Transformers: Hugging Face library for fine-tuning BERT.
  -Docker: Containerization for deployment.
  -HTML/CSS: Frontend for the web interface.


## 🛠 Installation  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/Named-Entity-Recognition-NER-with-BERT.git
cd Named-Entity-Recognition-NER-with-BERT
```
### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
🏃‍♂️ Running the API Locally
 1.Start the Flask app
   ```bash
      python app.py
  ```
2.Access the API
Open Postman or use curl to test the API:
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" \
-d '{"text": "Elon Musk founded SpaceX in California."}'
```
**Expected JSON Response:**
```output
{
  "text": "Elon Musk founded SpaceX in California.",
  "entities": [
    {"word": "Elon Musk", "entity": "PERSON"},
    {"word": "SpaceX", "entity": "ORG"},
    {"word": "California", "entity": "GPE"}
  ]
}
```

🐳 Dockerizing the API
1.Build the Docker Image
```bash
docker build -t ner-api .
```
2.Run the Docker Container
```bash
docker run -p 5000:5000 ner-api
```
3.Test the API Again
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" \
-d '{"text": "Elon Musk founded SpaceX in California."}'
```

📜 License
This project is open-source and available under the MIT License.

📬 Contact
If you have any questions or suggestions, feel free to open an issue or contact me at karthikeyareddy183@gmail.com.

