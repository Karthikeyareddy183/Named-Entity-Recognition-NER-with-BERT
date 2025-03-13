import streamlit as st
from transformers import pipeline

# Load the fine-tuned NER model
@st.cache_resource  # Cache the model to avoid reloading on every interaction
def load_model():
    model_path = r"D:\NER\ner-bert-model"  # Path to your fine-tuned model 
    ner_pipeline = pipeline("ner", model=model_path, tokenizer=model_path, aggregation_strategy="simple")
    return ner_pipeline

# Load the model
ner_pipeline = load_model()

# Streamlit app
def main():
    st.title("Named Entity Recognition (NER) with BERT")
    st.write("This app uses a fine-tuned BERT model to detect named entities in text.")

    # Input text box
    text = st.text_area("Enter your text here:", "John works at Google in New York.")

    # Predict button
    if st.button("Predict"):
        if text.strip():
            # Run the NER pipeline
            results = ner_pipeline(text)

            # Display results
            st.subheader("Predicted Entities:")
            for entity in results:
                st.write(f"**{entity['word']}** ({entity['entity_group']})")
        else:
            st.warning("Please enter some text to analyze.")

# Run the app
if __name__ == "__main__":
    main()