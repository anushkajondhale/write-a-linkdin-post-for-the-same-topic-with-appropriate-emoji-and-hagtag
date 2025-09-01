#!/bin/bash
# Load environment variables
export $(grep -v '^#' env.example.txt | xargs)
