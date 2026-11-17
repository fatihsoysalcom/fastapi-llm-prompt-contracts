# FastAPI LLM Prompt Contracts

This example demonstrates how to implement 'prompt contracts' using FastAPI and Pydantic. It defines structured input models for different prompt types, ensuring consistency and validation for LLM interactions. The service takes structured data and generates a standardized prompt string based on the contract.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Install dependencies: `pip install fastapi uvicorn pydantic`.
3. Run the server: `uvicorn main:app --reload`.
4. Access the interactive API docs at `http://127.0.0.1:8000/docs`.

## Original Article

This example accompanies the Turkish article: [FastAPI ile Güvenilir ve Ölçeklenebilir Prompt Sözleşme Servisi Nasıl Oluşturulur?](https://fatihsoysal.com/blog/fastapi-ile-guvenilir-ve-olceklenebilir-prompt-sozlesme-servisi-nasil-olusturulur/).

## License

MIT — see [LICENSE](LICENSE).
