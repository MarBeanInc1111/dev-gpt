TWITTER_APP = """
        Task:
        Create a Twitter clone using FastAPI and SQLite. The application should
        replicate the core features of Twitter, such as posting tweets, following users,
        and liking tweets.

        Requirements:
        - Use FastAPI as the web framework.
        - Use SQLite as the database.
        - Design RESTful endpoints for user interactions.
        - Implement account authentication and authorization.

        Running the App:
        The application must be set to run from the `main` function, using Uvicorn as the ASGI server.
        Ensure you import Uvicorn in your code and use it to run the app from `main`.
        """

ETH_PRICE = """
        Task:
        Predict the price of Ethereum (ETH) for the next week, and develop a detailed Dash app to
        showcase your research and calculations.

        Requirements:
        - Gather historical ETH price data for your model.
        - Use a suitable forecasting method to predict future prices.
        - Implement your forecast logic in a Python function.

        Dash App:
        - Create a Dash application to visualize your research and predictions.
        - The app should provide charts and graphs for users to understand the price trend.

        Note: You may need to install additional libraries for data analysis and visualization.
        """

MAKE_BLOCKCHAIN = """
        Task:
        Create a simple blockchain in Python and a FastAPI app to interact with it.

        Blockchain Requirements:
        - Implement standard blockchain features like creating blocks, validating the chain, and managing transactions.
        - Develop a proof-of-work algorithm to secure the chain.

        FastAPI App Interaction:
        - The FastAPI app should provide endpoints for interacting with the blockchain: viewing the chain, adding transactions, and mining new blocks.

        Running the App:
        Like the Twitter app, this blockchain application must initialize from a `main` function.
        Import Uvicorn within the code and configure it to run the app from `main`.
        """

SYSTEM_MESSAGE = """
Task:
Act as a senior python developer and provide code that is efficient, readable, and Pythonic.

Requirements:
- Write the code in a single file that is executable from a `main` function.
- Follow best practices for Python coding standards.

Output Format:
Include the commands to install any necessary dependencies, and provide the complete Python script.

Example:
```bash
pip install dependencies
```
```python
# Imports

def main():
    # Your code here

if __name__ == "__main__":
    main()
```
        
Note: It is essential to adhere to these guidelines to ensure the code runs correctly.
        """
