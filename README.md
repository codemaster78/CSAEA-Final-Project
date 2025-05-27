# 🚗 Rover Repair Garage: Driving Quiz

---

## Project Overview

Welcome to the **Driving Quiz**, a project designed for Tank's Rover Repair Garage! While Tank is a master mechanic, he also understands the importance of **well-prepared drivers** for his high-tech rovers. This interactive Python-based quiz serves as a fundamental **tutorial and assessment tool** for new apprentices and anyone looking to brush up on their driving knowledge.

Inspired by Tank's need to "teach apprentices the basics of rover guts," we've extended that concept to **road safety and driving regulations**. Think of it as the theoretical part of getting a rover out of the garage and safely onto the terrain. The quiz covers essential driving scenarios, rules, and best practices, aiming to instill crucial knowledge before anyone gets behind the wheel of one of Tank's prized machines.

---

## Features

* **Interactive Multiple-Choice Questions**: Each question presents four randomly ordered answer choices, ensuring a fresh experience with every play.
* **Real-time Feedback**: Get immediate feedback on whether your answer is correct or incorrect.
* **Score Tracking**: Your progress is tracked throughout the quiz, culminating in a final percentage score.
* **Clear Interface**: A simple and clean command-line interface makes the quiz easy to navigate.
* **Dynamic Question Presentation**: Questions and answers are displayed one at a time, providing a focused learning environment.
* **Automatic Screen Clearing**: The screen clears between questions for a tidy and readable experience.

---

## How to Play

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/codemaster78/CSAEA-Final-Project.git
    ```

2.  **Navigate to the Project Directory**:
    ```bash
    cd CSAEA-Final-Project
    ```

3.  **Run the Quiz**:
    ```bash
    python main.py
    ```

4.  **Answer the Questions**: For each question, type the letter corresponding to your chosen answer (a, b, c, or d) and press Enter.

5.  **Review Your Score**: At the end of the quiz, your total score will be displayed as a percentage.

---

## Code Structure

The project is straightforward and consists of a single Python script:

* `driving_quiz.py`: This file contains all the logic for the quiz, including question definitions, answer randomization, score tracking, and user interaction.

The core of the quiz lies within the `question()` function, which handles displaying the question and options, processing user input, and updating the score. A series of calls to this function define the quiz's content.

---

## Future Enhancements

While currently a foundational quiz, there are many avenues for expansion to make it even more robust for Tank's garage:

* **Expanded Question Database**: Implement a more extensive set of questions covering various driving topics, perhaps stored in an external file (e.g., CSV or JSON) for easier management.
* **Difficulty Levels**: Introduce different difficulty settings for apprentices at various stages of their learning.
* **Detailed Explanations**: Provide brief explanations for correct answers to enhance learning.
* **User Profiles**: Allow multiple apprentices to have their scores tracked and saved.
* **Graphical User Interface (GUI)**: Transition from a command-line interface to a more visually appealing GUI using libraries like Tkinter or PyQt.
* **Timed Questions**: Add a timer to questions to simulate real-world pressure or test quick recall.

---

This Driving Quiz is a simple yet effective tool to help **new rover operators gain confidence and knowledge** before they even touch a wrench. It's an essential step in Tank's mission to produce not just skilled mechanics, but also **responsible and knowledgeable drivers**.
