# Mini AI Chatbot

A lightweight AI chatbot built using GPT4All that runs locally on your machine. 

This project showcases problem-solving and adaptability: I navigated challenges such as configuring Python and Git PATHs, managing API keys, and exploring cloud vs. local solutions. After realizing that online API solutions required payment plans, I opted for a fully local implementation, demonstrating the ability to design and run an AI system independently, without relying on external services.

Designed as a personal project to demonstrate AI integration and Python development skills for a portfolio or CV.

## Features

- Runs locally without an API key
- Uses GPT4All (Phi-3 Mini Instruct) model
- Terminal-based user interface
- Easy to set up and run

## Project Structure

The project folder looks like this:

- `local_chatbot.py` — Main chatbot script  
- `requirements.txt` — Python dependencies  
- `README.md` — Project overview (this file)  
- `model/` — Folder for GPT4All model files (`.bin`)  

> Note: Create a `model` folder and place your GPT4All model there.

## Requirements

- Python 3.14+  
- GPT4All model file (`.bin`)  
- Python packages listed in `requirements.txt`  

Install dependencies:

```bash
pip install -r requirements.txt
