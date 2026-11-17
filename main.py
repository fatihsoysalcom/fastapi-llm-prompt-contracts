from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(
    title="Prompt Contract Service",
    description="A service to generate standardized prompts based on predefined contracts for LLMs."
)

# This Pydantic model represents a 'Prompt Contract' for a summarization task.
# It defines the expected structure and validation rules for inputs needed to create this prompt.
class SummarizationPromptContract(BaseModel):
    text_content: str = Field(..., description="The text content to be summarized.")
    summary_length: str = Field("medium", description="Desired length of the summary (e.g., 'short', 'medium', 'long').")
    output_format: str = Field("paragraph", description="Desired output format (e.g., 'paragraph', 'bullet_points').")
    language: str = Field("English", description="Target language for the summary.")

    class Config:
        schema_extra = {
            "example": {
                "text_content": "Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals.",
                "summary_length": "short",
                "output_format": "paragraph",
                "language": "English"
            }
        }

# This Pydantic model represents another 'Prompt Contract' for a creative writing task.
class CreativeWritingPromptContract(BaseModel):
    topic: str = Field(..., description="The main topic or theme for the creative writing.")
    genre: str = Field("fantasy", description="The genre of the writing (e.g., 'fantasy', 'sci-fi', 'mystery').")
    word_count_min: int = Field(100, description="Minimum word count for the output.")
    word_count_max: int = Field(300, description="Maximum word count for the output.")

    class Config:
        schema_extra = {
            "example": {
                "topic": "A lone astronaut discovering a new planet",
                "genre": "sci-fi",
                "word_count_min": 150,
                "word_count_max": 250
            }
        }

@app.post("/generate-summary-prompt")
async def generate_summary_prompt(contract: SummarizationPromptContract):
    """
    Generates a standardized prompt string for a summarization task based on the provided contract.
    """
    # The 'contract' object has been validated by Pydantic/FastAPI against the SummarizationPromptContract.
    # We use its validated fields to construct the final prompt string, ensuring consistency.
    prompt_template = (
        f"Please summarize the following text in a {contract.summary_length} "
        f"{contract.output_format} in {contract.language}. "
        f"Text to summarize: \"{contract.text_content}\"
    )
    return {"generated_prompt": prompt_template}

@app.post("/generate-creative-writing-prompt")
async def generate_creative_writing_prompt(contract: CreativeWritingPromptContract):
    """
    Generates a standardized prompt string for a creative writing task based on the provided contract.
    """
    # Similarly, this endpoint uses the CreativeWritingPromptContract for validation and prompt generation.
    prompt_template = (
        f"Write a {contract.genre} story about '{contract.topic}'. "
        f"The story should be between {contract.word_count_min} and {contract.word_count_max} words long."
    )
    return {"generated_prompt": prompt_template}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
