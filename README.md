# Scones Unlimited: Machine Learning Workflow on AWS SageMaker

## Project Overview

This project is final project of the AWS Machine Learning Fundamentals Udacity Nanodegree program, where the goal is to build a machine learning (ML) workflow for a logistics company, **Scones Unlimited**. The project focuses on developing an image classification model that identifies the type of vehicle used by delivery drivers (bicycles vs. motorcycles) to optimize delivery routes. This solution enhances the company’s operations by ensuring that delivery tasks are assigned based on the vehicle type, improving efficiency and customer satisfaction.

## Project Introduction

### Background

Image classifiers play a crucial role in computer vision, helping identify the content of images across various industries. They are used in advanced technologies such as autonomous vehicles, augmented reality, eCommerce platforms, and diagnostic medicine. In this project, as a Machine Learning Engineer (MLE) for Scones Unlimited, I was tasked with shipping an image classification model to help the company optimize its delivery operations.

The image classification model can be used in multiple scenarios within the company’s operations, such as:

- Detecting people and vehicles in roadway video feeds
- Supporting routing for social media engagement
- Detecting defects in scones, and more

### Objective

The primary objective was to create a scalable and secure model that can be deployed on-demand and monitored for performance. The model was trained to distinguish between bicycles and motorcycles, allowing Scones Unlimited to route deliveries more effectively. Bicycles were assigned to nearby orders, while motorcyclists were given farther deliveries.

## Project Workflow

The project was divided into several key steps:

### 1. Data Staging

The first step involved setting up the data staging environment, which included data extraction, transformation, and loading (ETL) to prepare the data for the machine learning process.

### 2. Model Training and Deployment

The image classification model was trained and deployed using **Amazon SageMaker**. The model was fine-tuned and optimized for accurate predictions, allowing it to reliably distinguish between bicycles and motorcycles.

### 3. Building Supporting Services

To support the model, three **AWS Lambda functions** were created:

- **Function 1:** Returns an object as `image_data` in an event to the Step Function.
- **Function 2:** Handles the image classification process.
- **Function 3:** Filters out low-confidence inferences to ensure the reliability of the results.

### 4. Step Function Workflow

The Lambda functions were composed together into a **Step Function** workflow, creating a seamless, event-driven application. This workflow ensures the model operates smoothly in a production environment, scaling as needed to meet demand.

### 5. Testing and Evaluation

Extensive testing and evaluation were conducted to validate the model’s performance and the robustness of the entire workflow. This step ensured that the solution was ready for deployment in a real-world scenario.

### 6. Cleanup of Cloud Resources

Finally, cloud resources used during the project were cleaned up to maintain an organized and cost-effective working environment.

## Technologies Used

- **AWS SageMaker**: For building, training, and deploying the machine learning model.
- **AWS Lambda**: For creating serverless functions to support the ML workflow.
- **AWS Step Functions**: For composing and managing the workflow of the Lambda functions.
- **Python**: For coding and scripting throughout the project.

## Acknowledgments

I would like to extend my sincere gratitude to:

- **Fady Morris**, my session lead, for his guidance, starter codes, and insightful videos that made this project a success.

## Conclusion

This project was a significant learning experience, providing hands-on expertise in building, deploying, and managing machine learning models on AWS. The skills and knowledge gained from this project will be instrumental in my future endeavors as a Machine Learning Engineer.
