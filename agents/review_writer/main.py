import sys
import os

# Use the following to write a shoe review. Change the shoe names in the shoe_review.py file.
from agents.review_writer.shoe_review import input_prompt, research, style, post_name

# Use the following to write a comparison review. Change the shoe names in the comparison_review.py file.
# from agents.review_writer.comparison_review import input_prompt, research, style, post_name

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from graph import create_workflow

# Load environment variables from .env file
load_dotenv()
app = create_workflow()

inputs = {"initial_prompt": input_prompt,
          "research": research,
          "style": style,
          "num_steps": 0,
          "post_name": post_name}

output = app.invoke(inputs)
