def write_markdown_file(content, filename, directory="output"):
  """Writes the given content as a markdown file to the local directory.

  Args:
    content: The string content to write to the file.
    filename: The filename to save the file as.
  """
  with open(f"{directory}/{filename}.md", "w") as f:
    f.write(content)