import sys
import os

from agents.review_writer.brr_nick import style
# from agents.review_writer.brr_review import structure
# Use the following to write a shoe review. Change the shoe names in the shoe_review.py file.
# from agents.review_writer.shoe_review import subject, research, post_name

# Use the following to write a comparison review. Change the shoe names in the comparison_review.py file.
# from agents.review_writer.comparison_review import subject, research, post_name

# Use the following to write a shoe review. Change the shoe names in the shoe_review.py file.
from agents.review_writer.info_post import subject, research, structure, post_name

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from graph import create_workflow

# Load environment variables from .env file
load_dotenv()
app = create_workflow()

inputs = {"subject": subject,
          "research": research,
          "style": style,
          "structure": structure,
          "num_steps": 0,
          "post_name": post_name}

output = app.invoke(inputs)
