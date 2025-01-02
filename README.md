# Blog Post Writer

This is a tool adjusted from https://github.com/samwit/agent_tutorials/tree/main/agent_writer to generate blog posts about running shoes. It uses the OpenAI API to generate content based on a set of prompts and instructions. The generated content is then saved in Markdown format.

## Usage

1. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
   
2. Install the required dependencies:
   ```
    pip install -r requirements.txt
   ```

3. Adjust the input data in agents/review_writer/shoe_review.py.

4. Run the main script to generate content:
   ```
   python agents/review_writer/main.py
   ```
   
5. Review the generated content in the output folder. `agents/review_writer/output/`




