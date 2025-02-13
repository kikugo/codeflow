# Enhanced CodeFlow

This project is an enhanced version of [CodeFlow](https://github.com/rajtilakjee/codeflow), originally created by [Rajtilak](https://github.com/rajtilakjee). It provides a typewriter effect for displaying code, making it ideal for tutorials, presentations, and educational content. This version includes several new features and improvements.

**Original Project:** [CodeFlow by Rajtilak](https://github.com/rajtilakjee/codeflow)

**License:** This project is licensed under the GNU General Public License version 3 (GPL-3.0). See the [LICENSE](LICENSE) file for details.

## Enhancements

This enhanced version of CodeFlow includes the following new features:

*   **Delay Control:** Adjust the typing speed of the typewriter effect using a slider.
*   **Line Number Toggle:** Show or hide line numbers in the code display.
*   **File Upload:** Upload code files directly instead of just pasting text.  Supports various programming languages.
*   **Theme Switching (Light/Dark):** Switch between light and dark themes for better visual comfort.
*   **Syntax Highlighting Theme Selection:** Choose from different syntax highlighting themes (e.g., Monokai, Dracula, GitHub Dark) to customize the code's appearance.
*   **Input Validation:** The app checks for code input and language selection before running the effect, preventing errors.
*   **Error Handling:** Includes `try...except` blocks to gracefully handle potential errors during code rendering.
*   **Progress Message:** Displays a "Typing..." message with progress indication during the typewriter effect.
*   **"Replay" Button:** Replay the typewriter effect without switching tabs.
*   **"Reset" Button:** Clear the code input and language selection.
*   **Word Wrap Toggle:** Enable or disable word wrapping for long lines of code.
*   **Code Refactoring:** The code has been reorganized into functions for better readability, maintainability, and testability. Includes type hints and comments.
*   **Embedded CSS:** Styling is handled directly within the `app.py` file, eliminating the need for a separate `style.css` file.
*   **Automatic Language Detection (Basic):** Attempts to detect the programming language based on the uploaded file's extension.

## Installation and Usage

To run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) (version 3.7 or higher is recommended) installed on your computer.

1.  **Clone the repository:**

    ```bash
    git clone <your_forked_repo_url>  # Replace with YOUR forked repository URL
    cd <your_repo_name>  # e.g., cd codeflow
    ```

2.  **Create and Activate a Conda Environment (Recommended):**

    It's highly recommended to use a Conda environment to manage dependencies:

    ```bash
    conda create -n codeflow-env python=3.9  # Or your preferred Python version
    conda activate codeflow-env
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App:**

    ```bash
    streamlit run app.py
    ```

    This will start the Streamlit server, and the app will open in your web browser.

## Usage Instructions

1.  **Select a Programming Language:** Use the dropdown menu in the "Data" tab to choose the language of the code you want to display.
2.  **Enter or Upload Code:**
    *   **Paste Code:** Paste your code directly into the text area.
    *   **Upload File:** Click the "Browse files" button to upload a code file. The app will attempt to detect the language automatically.
3.  **Adjust Settings:**
    *   **Typing Speed (Delay):** Use the slider to control the speed of the typewriter effect.
    *   **Show Line Numbers:** Toggle line numbers on or off.
    *   **Wrap Lines**: Toggle word wrap on or off.
    *   **Syntax Highlighting Theme:** Select a theme from the dropdown.
    *   **Dark Mode:** Toggle between light and dark themes.
4.  **View the Effect:** Switch to the "Effect" tab to see the typewriter effect in action.
5.  **Replay:** Click the "Replay" button to run the effect again.
6.  **Reset:** Click the "Reset" button to clear the input.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name` or `git checkout -b bugfix/your-bug-fix`.
3.  Make your changes and commit them with clear, descriptive commit messages.
4.  Push your branch to your forked repository: `git push origin feature/your-feature-name`.
5.  Create a pull request from your branch to the `main` branch of this repository.

Please ensure your code adheres to the GPL-3.0 license.

## Acknowledgements

This project is built upon the original CodeFlow by [Rajtilak](https://github.com/rajtilakjee). Thanks to Rajtilak for creating the original application!