import os
import re
import subprocess
from venv import create

from dotenv import load_dotenv
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from prompts import SYSTEM_MESSAGE

load_dotenv()
my_secret = os.environ['OPENAI_API_KEY']


class PythonDevAssistant:

  def __init__(self):
    self.venv_dir = "./venv"
    self.chat, self.messages = self.initialize_chat(), [
        SystemMessage(content=SYSTEM_MESSAGE)
    ]

  def initialize_chat(self):
    if not os.path.isdir(self.venv_dir):
      create(self.venv_dir, with_pip=True)
    return ChatOpenAI(streaming=True,
                      callbacks=[StreamingStdOutCallbackHandler()],
                      temperature=0,
                      model="gpt-4")

  def create_venv(self):
    create(self.venv_dir, with_pip=True)

  def add_msg(self, message, role="human"):
    self.messages.append(
        HumanMessage(content=message) if role == "human" else SystemMessage(
            content=message))

  def extract_code(self, response: str):
    return {
        t: re.findall(rf"```{t}\s*([\s\S]*?)```", response)
        for t in ["python", "bash"]
    }

  def install_deps(self, dependencies):
    if dependencies:
      for dep in dependencies:
        if dep.strip():
          subprocess.check_call(
              [f"{self.venv_dir}/bin/python", "-m", "pip", "install"] +
              dep.split())

  def run_script(self, script_path):
    return subprocess.run([f"{self.venv_dir}/bin/python", script_path],
                          capture_output=True,
                          text=True,
                          check=True)

  def generate_code(self, prompt: str, attempts=5):
    self.add_msg(prompt)
    for _ in range(attempts):
      code = self.extract_code(self.chat(self.messages).content)
      self.install_deps(code.get("bash", []))
      python_code = code.get("python", [])
      if not python_code:
        raise ValueError("No python code generated.")
      self.add_msg(f"this is the code generated: {python_code[0]}")
      with open("temp.py", "w") as f:
        f.write(python_code[0])
      try:
        output = self.run_script("temp.py").stdout
        print(output)
        improvement = input(
            "How can I improve the code? enter the code or type 'no' to finish:"
        )
        if improvement.lower() == "no":
          return output
        self.add_msg(improvement)
      except subprocess.CalledProcessError as e:
        self.add_msg(
            f"I got an error when running the code. Can you help me fix it? {e}"
        )
    raise ValueError("Max attempts reached. Unable to generate valid code.")


if __name__ == "__main__":
  assistant = PythonDevAssistant()
  print(assistant.generate_code(input("Enter a prompt: ")))
