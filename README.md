# University Progression Prediction Program

This Python program predicts progression outcomes for students at the end of each academic year based on the credit information provided. The progression outcomes are determined according to the University regulations outlined in Table 1.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Validation](#validation)
- [Histogram](#histogram)
- [Extensions](#extensions)
- [How to Contribute](#how-to-contribute)
- [Usage](#usage)

## Description

The University Progression Prediction Program is designed to assist staff members in predicting the progression outcomes of students based on their credit information. The program follows the guidelines specified by the University regulations and provides accurate predictions for various scenarios.

## Features

- Predict progression outcomes for individual students.
- Validate input data to ensure correctness.
- Generate a horizontal histogram displaying the distribution of progression outcomes.
- Easily extendable for additional features and enhancements.

## Validation

The program performs validation checks to ensure the input data is correct:

- Checks for integer input.
- Verifies that credit values are within the specified range.
- Ensures that the total credits sum up to 120.

## Histogram

The program generates a horizontal histogram displaying the distribution of progression outcomes. Each category (e.g., Progress, Module retriever) is represented by stars (*) corresponding to the number of students in that category.

## Extensions

- **Part 2 - Vertical Histogram**: Extend the program to generate a vertical histogram.
- **Part 3 - List/Tuple/Directory**: Save input progression data to a list, tuple, or directory and access the stored data to print in a specific format.
- **Part 4 - Text File**: Save input progression data to a text file and access the stored data to print it out.

## How to Contribute

Contributions to the University Progression Prediction Program are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.


## Usage

To use the program, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python program using a Python interpreter.

Example:

```bash
python progression_prediction.py 

