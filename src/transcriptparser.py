import pdftotext
import openai
import re
import logging
import json
from tiktoken_counter import count_tokens


class TranscriptParser:
    def __init__(self, OPENAI_API_KEY):
        openai.api_key = OPENAI_API_KEY
        self.prompt_questions = """Summarize the text below into a JSON with exactly the following structure {first_name, last_name, full_name, university, education_level (BS, MS, or PhD), graduation_year, graduation_month, majors, GPA, Courses and grades using the following format: {course: <course_name>, grade: <grade>}, {course: <course_name>, grade: <grade>}, ...}
"""
        logging.basicConfig(filename="logs/parser.log", level=logging.DEBUG)
        self.logger = logging.getLogger()

    def pdf2string(self: object, pdf_path: str) -> str:
        with open(pdf_path, "rb") as f:
            pdf = pdftotext.PDF(f)
        pdf_str = "\n\n".join(pdf)
        pdf_str = re.sub("\s[,.]", ",", pdf_str)
        pdf_str = re.sub("[\n]+", "\n", pdf_str)
        pdf_str = re.sub("[\s]+", " ", pdf_str)
        pdf_str = re.sub("http[s]?(://)?", "", pdf_str)
        return pdf_str

    def query_completion(
        self: object,
        prompt: str,
        engine: str = "text-curie-001",
        temperature: float = 0.0,
        max_tokens: int = 100,
        top_p: int = 1,
        frequency_penalty: int = 0,
        presence_penalty: int = 0,
    ) -> object:
        self.logger.info(f"query_completion: using {engine}")

        estimated_prompt_tokens = count_tokens(prompt, engine)
        estimated_answer_tokens = max_tokens - estimated_prompt_tokens
        self.logger.info(
            f"Tokens: {estimated_prompt_tokens} + {estimated_answer_tokens} = {max_tokens}"
        )

        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=estimated_answer_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )
        return response

    def transcript(self: object, pdf_path: str) -> dict:
        transcript = {}
        pdf_str = self.pdf2string(pdf_path)
        print(pdf_str)
        prompt = self.prompt_questions + "\n" + pdf_str

        engine = "text-davinci-002"
        max_tokens = 4097

        response = self.query_completion(prompt, engine=engine, max_tokens=max_tokens)
        response_text = response["choices"][0]["text"].strip()
        print(response_text)
        transcript = json.loads(response_text)
        return transcript
