# Crypto Trading Bot

## Overview

This project automates cryptocurrency trading based on signals from TradingView alerts. It uses Coinbase for executing trades and GitHub for version control and collaboration.

## Files

- **`main.py`**: The Python script responsible for executing the buy/sell actions based on TradingView alerts.
- **`pairs.json`**: Contains the cryptocurrency pairs that the bot will trade (e.g., BTC/USD, ETH/USD).
- **`parameters.json`**: Configuration file containing settings like trade sizes and other parameters.
- **`render.yaml`**: Configuration file for deploying the project on Render (if using Render for hosting).
- **`.env`**: Stores environment variables such as API keys and other secrets.

## Prerequisites

Before running the bot, you need:

- A **Coinbase Pro account**.
- A **TradingView account** for setting up alerts.
- A **GitHub account** for version control.
- **Python 3.7+** and the necessary libraries (see `requirements.txt`).

## Setup

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <project-directory>
